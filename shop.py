import streamlit as st
import requests

# إعدادات تليغرام الخاصة بك
TELEGRAM_TOKEN = "8966476087:AAFFcvYyi6eOh37KDr8vDZ_BiJJU4dI7uDA"
TELEGRAM_CHAT_ID = "8966476087"

def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

# إعدادات الصفحة
st.set_page_config(page_title="متجر توفيق للرياضيات", page_icon="📖", layout="centered")

# عنوان المتجر
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛒 متجر لاقتناء كتاب توفيق للرياضيات</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>مرحباً بك في المتجر الإلكتروني، يرجى ملء معلوماتك لطلب الكتب</p>", unsafe_allow_html=True)
st.write("---")

# المدخلات
name = st.text_input("👤 أدخل اسمك الكامل:")
phone = st.text_input("📞 أدخل رقم هاتفك:")
wilaya = st.text_input("📍 أدخل ولايتك أو بلدليتك (مثال: أفلو):")

st.write("### 📚 اختر الكتب بالنقر على المربعات حذاها:")
book1 = st.checkbox("كتاب الدوال (400 دج)")
book2 = st.checkbox("كتاب المتتاليات (400 دج)")

# حساب الأسعار والتوصيل لـ أفلو برك
سعر_الكتب = 0
if book1: سعر_الكتب += 400
if book2: سعر_الكتب += 400

سعر_التوصيل = 0
# الحساب لأفلو برك بـ 1000 دج (10 آلاف)
if wilaya and "أفلو" in wilaya:
    سعر_التوصيل = 1000

الإجمالي = سعر_الكتب + سعر_التوصيل

# عرض الحسبة الأولية للمشتري قبل الإرسال
if سعر_الكتب > 0:
    st.write("---")
    st.write(f"**💰 سعر الكتب:** {سعر_الكتب} دج")
    if سعر_التوصيل > 0:
        st.write(f"**🚚 سعر التوصيل (أفلو):** {سعر_التوصيل} دج (10 آلاف)")
    else:
        st.write(f"**🚚 سعر التوصيل:** سيتم تحديده لاحقاً عبر الهاتف لباقي المناطق")
    st.markdown(f"### 🛑 المبلغ الإجمالي المبدئي: **{الإجمالي} دج**")
    st.write("---")

submit_button = st.button("🚀 إرسال الطلب الآن")

# معالجة الطلب عند الضغط على الزر
if submit_button:
    if not name or not phone or not wilaya:
        st.error("❌ من فضلك املأ جميع الخانات (الاسم، الهاتف، والولاية) لإتمام الطلب.")
    elif not book1 and not book2:
        st.error("❌ من فضلك اختر كتاباً واحداً على الأقل.")
    else:
        # تحديد الكتب المختارة
        selected_books = []
        if book1: selected_books.append("كتاب الدوال")
        if book2: selected_books.append("كتاب المتتاليات")
        books_text = ", ".join(selected_books)
        
        # تجهيز رسالة التليغرام المريغلة
        tg_message = (
            "🔔 *طلب جديد في المتجر!* 🔔\n\n"
            f"👤 *الاسم الكامل:* {name}\n"
            f"📞 *رقم الهاتف:* {phone}\n"
            f"📍 *المكان:* {wilaya}\n"
            f"📚 *الكتب المطلوبة:* {books_text}\n"
            f"💰 *المبلغ الإجمالي:* {الإجمالي} دج"
        )
        
        # إرسال للتليغرام
        send_telegram_notification(tg_message)
            
        st.success(f"✅ تم إرسال طلبيتك بنجاح يا {name}! سنتصل بك قريباً لتأكيد الشحن.")
        st.balloons()
        
        # 🧾 الفاتورة النهائية الرسمية التي تظهر للمشتري في الموقع
        st.markdown("""
        <div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border: 2px dashed #1E3A8A; margin-top: 20px;'>
            <h3 style='text-align: center; color: #1E3A8A; margin-top: 0;'>🧾 الفاتورة الرسمية للطلب</h3>
            <p><b>👤 الاسم الكامل:</b> {}</p>
            <p><b>📞 رقم الهاتف:</b> {}</p>
            <p><b>📍 العنوان/الولاية:</b> {}</p>
            <p><b>📚 الكتب المطلوبة:</b> {}</p>
            <hr style='border-top: 1px dashed #9CA3AF;'>
            <p><b>💰 سعر الكتب:</b> {} دج</p>
            <p><b>🚚 سعر التوصيل:</b> {} دج</p>
            <h4 style='color: #B91C1C; margin-bottom: 0;'>🛑 المبلغ الإجمالي المستحق: {} دج</h4>
        </div>
        """.format(name, phone, wilaya, books_text, سعر_الكتب, سعر_التوصيل if سعر_التوصيل > 0 else "سيحدد لاحقاً", الإجمالي), unsafe_allow_html=True)
