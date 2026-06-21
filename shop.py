import streamlit as st
import requests

# إعدادات تليغرام الخاصة بك بعد التعديل
TELEGRAM_TOKEN = "8857487956:AAG1Ylg0TnedERGYM7TcsPnu24wtAPHUCy8"
TELEGRAM_CHAT_ID = "8857487956"

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

# المدخلات الأساسية
name = st.text_input("👤 أدخل اسمك الكامل:")
phone = st.text_input("📞 أدخل رقم هاتفك:")
wilaya = st.text_input("📍 أدخل ولايتك أو بلدليتك (مثال: أفلو، الجزائر، الجلفة...):")

st.write("### 📚 اختر الكتب بالنقر على المربعات حذاها:")
book1 = st.checkbox("كتاب الدوال (400 دج)")
book2 = st.checkbox("كتاب المتتاليات (400 دج)")
book3 = st.checkbox("كتاب الأعداد المركبة (400 دج)")
book4 = st.checkbox("كتاب الاحتمالات (400 دج)")

# حساب سعر الكتب
سعر_الكتب = 0
if book1: سعر_الكتب += 400
if book2: سعر_الكتب += 400
if book3: سعر_الكتب += 400
if book4: سعر_الكتب += 400

# إعداد متغيرات التوصيل
shipping_cost = 0
shipping_method = ""

# شروط التوصيل الذكية (تتعرف على أفلو بكل الأشكال الممكنة)
if wilaya:
    w_clean = wilaya.strip().lower()
    w_clean = w_clean.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    
    if "افلو" in w_clean:
        st.write("### 🚚 خيارات الاستلام في أفلو:")
        aflo_option = st.radio(
            "اختر كيف تريد استلام كتبك:",
            ("توصيل منزلي داخل أفلو (1000 دج / 10 آلاف)", "أستلم الكتاب بنفسي (0 دج / يجي يديه روحو)")
        )
        if "توصيل" in aflo_option:
            shipping_cost = 1000
            shipping_method = "توصيل منزلي داخل أفلو (10 آلاف)"
        else:
            shipping_cost = 0
            shipping_method = "استلام شخصي من طرف المشتري (يجي يديه روحو)"
    else:
        st.write("### 🚚 اختر نوع التوصيل لولايتك عبر يالدين:")
        delivery_option = st.radio(
            "اختر مكاناً لاستلام الطرد:",
            ("توصيل إلى المكتب (4000 دج / 40 ألف)", "توصيل إلى باب المنزل (7000 دج / 70 ألف)")
        )
        if "المكتب" in delivery_option:
            shipping_cost = 4000
            shipping_method = "توصيل للمكتب عبر يالدين (40 ألف)"
        else:
            shipping_cost = 7000
            shipping_method = "توصيل لباب المنزل عبر يالدين (70 ألف)"

الإجمالي = سعر_الكتب + shipping_cost

# عرض الحسبة المبدئية قبل الإرسال
if سعر_الكتب > 0:
    st.write("---")
    st.write(f"**💰 سعر الكتب:** {سعر_الكتب} دج")
    st.write(f"**🚚 طريقة الاستلام الحالية:** {shipping_method}")
    st.markdown(f"### 🛑 المبلغ الإجمالي المبدئي: **{الإجمالي} دج**")
    st.write("---")

submit_button = st.button("🚀 إرسال الطلب الآن")

# معالجة الضغط على الزر
if submit_button:
    if not name or not phone or not wilaya:
        st.error("❌ من فضلك املأ جميع الخانات لإتمام الطلب.")
    elif not book1 and not book2 and not book3 and not book4:
        st.error("❌ من فضلك اختر كتاباً واحداً على الأقل.")
    else:
        selected_books = []
        if book1: selected_books.append("كتاب الدوال")
        if book2: selected_books.append("كتاب المتتاليات")
        if book3: selected_books.append("كتاب الأعداد المركبة")
        if book4: selected_books.append("كتاب الاحتمالات")
        books_text = ", ".join(selected_books)
        
        tg_message = (
            "🔔 *طلب جديد في المتجر!* 🔔\n\n"
            f"👤 *الاسم الكامل:* {name}\n"
            f"📞 *رقم الهاتف:* {phone}\n"
            f"📍 *المكان:* {wilaya}\n"
            f"🚚 *طريقة الاستلام:* {shipping_method}\n"
            f"📚 *الكتب المطلوبة:* {books_text}\n"
            f"💰 *الإجمالي المستحق:* {الإجمالي} دج"
        )
        
        send_telegram_notification(tg_message)
            
        st.success(f"✅ تم إرسال طلبيتك بنجاح يا {name}!")
        st.balloons()
        
        st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border: 2px dashed #1E3A8A; margin-top: 20px; text-align: right;' dir='rtl'>
            <h3 style='text-align: center; color: #1E3A8A; margin-top: 0;'>🧾 الفاتورة الرسمية للطلب</h3>
            <p><b>👤 الاسم الكامل:</b> {name}</p>
            <p><b>📞 رقم الهاتف:</b> {phone}</p>
            <p><b>📍 العنوان/الولاية:</b> {wilaya}</p>
            <p><b>📚 الكتب المطلوبة:</b> {books_text}</p>
            <hr style='border-top: 1px dashed #9CA3AF;'>
            <p><b>💰 سعر الكتب:</b> {سعر_الكتب} دج</p>
            <p><b>🚚 طريقة التوصيل:</b> {shipping_method}</p>
            <h4 style='color: #B91C1C; margin-bottom: 0;'>🛑 المبلغ الإجمالي المستحق: {الإجمالي} دج</h4>
        </div>
        """, unsafe_allow_html=True)
