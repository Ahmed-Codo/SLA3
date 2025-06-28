# استخدم صورة Python الرسمية كقاعدة
FROM python:3.11-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# تثبيت الأدوات الأساسية
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملفات المشروع
COPY . /app

# تثبيت الحزم المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# فتح المنفذ 5000
EXPOSE 5000

# تشغيل التطبيق
CMD ["python", "api.py"]