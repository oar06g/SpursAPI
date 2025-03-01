// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"
#include <wbemidl.h>
#include <comdef.h>
#include <string>
#include <codecvt>
#include <locale>

BOOL APIENTRY DllMain(HMODULE hModule,
    DWORD  ul_reason_for_call,
    LPVOID lpReserved) {
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

#pragma comment(lib, "wbemuuid.lib")
#define EXPORT __declspec(dllexport)

std::string ConvertBSTRToUTF8(BSTR bstr) {
    if (!bstr) return "Conversion Failed";

    std::wstring wstr(bstr, SysStringLen(bstr));  // تحويل BSTR إلى std::wstring
    std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
    return converter.to_bytes(wstr);  // تحويل wstring إلى utf-8
}

extern "C" EXPORT const char* GetSerialNumber() {
    HRESULT hres;
    static std::string serialNumber = "Not Found";

    hres = CoInitializeEx(0, COINIT_MULTITHREADED);
    if (FAILED(hres)) return "COM Initialization Failed";

    hres = CoInitializeSecurity(NULL, -1, NULL, NULL, RPC_C_AUTHN_LEVEL_DEFAULT,
        RPC_C_IMP_LEVEL_IMPERSONATE, NULL, EOAC_NONE, NULL);
    if (FAILED(hres)) {
        CoUninitialize();
        return "Security Initialization Failed";
    }

    IWbemLocator* pLocator = NULL;
    hres = CoCreateInstance(CLSID_WbemLocator, 0, CLSCTX_INPROC_SERVER, IID_IWbemLocator,
        (LPVOID*)&pLocator);
    if (FAILED(hres)) {
        CoUninitialize();
        return "WbemLocator Creation Failed";
    }

    IWbemServices* pServices = NULL;
    hres = pLocator->ConnectServer(BSTR(L"ROOT\\CIMV2"), NULL, NULL, 0, NULL, 0, 0, &pServices);
    if (FAILED(hres)) {
        pLocator->Release();
        CoUninitialize();
        return "WMI Connection Failed";
    }

    hres = CoSetProxyBlanket(pServices, RPC_C_AUTHN_WINNT, RPC_C_AUTHZ_NONE, NULL,
        RPC_C_AUTHN_LEVEL_CALL, RPC_C_IMP_LEVEL_IMPERSONATE, NULL, EOAC_NONE);
    if (FAILED(hres)) {
        pServices->Release();
        pLocator->Release();
        CoUninitialize();
        return "Proxy Blanket Setting Failed";
    }

    IEnumWbemClassObject* pEnumerator = NULL;
    hres = pServices->ExecQuery(BSTR(L"WQL"), BSTR(L"SELECT SerialNumber FROM Win32_BIOS"),
        WBEM_FLAG_FORWARD_ONLY | WBEM_FLAG_RETURN_IMMEDIATELY, NULL, &pEnumerator);
    if (FAILED(hres)) {
        pServices->Release();
        pLocator->Release();
        CoUninitialize();
        return "Query Execution Failed";
    }

    IWbemClassObject* pClassObject = NULL;
    ULONG uReturn = 0;
    while (pEnumerator) {
        HRESULT hr = pEnumerator->Next(WBEM_INFINITE, 1, &pClassObject, &uReturn);
        if (0 == uReturn) break;

        VARIANT vtProp;
        hr = pClassObject->Get(L"SerialNumber", 0, &vtProp, 0, 0);
        if (SUCCEEDED(hr)) serialNumber = ConvertBSTRToUTF8(vtProp.bstrVal);
        VariantClear(&vtProp);
        pClassObject->Release();
    }

    pEnumerator->Release();
    pServices->Release();
    pLocator->Release();
    CoUninitialize();

    return serialNumber.c_str();
}
