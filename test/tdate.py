from datetime import datetime

def check_time_difference(input_date: str) -> str:
    # تحويل التاريخ المدخل إلى كائن datetime
    input_dt = datetime.strptime(input_date, "%Y-%m-%d")
    
    # الحصول على الوقت الحالي
    now = datetime.now()
    
    # حساب الفرق بين التاريخين بالأيام
    difference_days = (now - input_dt).days
    
    # تحويل الفرق إلى أشهر تقريبية
    difference_months = difference_days / 30  # باعتبار كل شهر 30 يومًا تقريبيًا
    
    # التحقق من الفرق الزمني
    if difference_months > 1:
        return "above month"
    elif difference_months == 1:
        return "one month"
    else:
        return "down"

# تجربة الدالة
input_date = "2025-01-31"
result = check_time_difference(input_date)
print(result)
