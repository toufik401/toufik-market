import streamlit as st
import requests
BOT_TOKEN = "8640762406:AAEUmaIhfoWA0ur4GArRktsiNACNxccnqq0"
CHAT_ID = "7055252264"
def send_telegram_order(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    requests.post(url, data=payload)
st.set_page_config(page_title="متجر توفيق للرياضيات", page_icon="📖", layout="centered")
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛒 متجر لاقتناء كتاب توفيق للرياضيات</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>مرحباً بك في المتجر الإلكتروني، يرجى ملء معلوماتك لطلب الكتب</p>", unsafe_allow_html=True)
st.write("---")
name = st.text_input("👤 أدخل اسمك الكامل:")
phone = st.text_input("📞 أدخل رقم هاتفك:")
wilaya = st.text_input("📍 أدخل ولايتك أو بلدليتك (مثال: أفلو، الجزائر، الجلفة...):")
st.write("### 📚 اختر الكتب بالنقر على المربعات حذاها:")
book1 = st.checkbox("كتاب الدوال (400 دج / 40 ألف)")
book2 = st.checkbox("كتاب المتتاليات (400 دج / 40 ألف)")
book3 = st.checkbox("كتاب الأعداد المركبة (400 دج / 40 ألف)")
book4 = st.checkbox("كتاب الاحتمالات (400 دج / 40 ألف)")
if book1: سعر_الكتب += 400
if book2: سعر_الكتب += 400
if book3: سعر_الكتب += 400
if book4: سعر_الكتب += 400
shipping_cost = 0
shipping_method = ""
if wilaya:
    w_clean = wilaya.strip().lower()
    w_clean = w_clean.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    if "افلو" in w_clean:
        st.write("### 🚚 خيارات الاستلام في أفلو:")
        aflo_option = st.radio(
            "اختر كيف تريد استلام كتبك:",
            ("توصيل منزلي داخل أفلو (100 دج / 10 آلاف)", "أستلم الكتاب بنفسي (0 دج / يجي يديه روحو)")
        )
        if "توصيل" in aflo_option:
            shipping_cost = 100
            shipping_method = "توصيل منزلي داخل أفلو (10 آلاف)"
        else:
            shipping_cost = 0
            shipping_method = "استلام شخصي من طرف المشتري (يجي يديه روحو)"
    else:
        st.write("### 🚚 اختر نوع التوصيل لولايتك عبر يالدين:")
        delivery_option = st.radio(
            "اختر مكاناً لاستلام الطرد:",
            ("توصيل إلى المكتب (400 دج / 40 ألف)", "توصيل إلى باب المنزل (700 دج / 70 ألف)")
        )
        if "المكتب" in delivery_option:
            shipping_cost = 400
            shipping_method = "توصيل للمكتب عبر يالدين (40 ألف)"
        else:
            shipping_cost = 700
            shipping_method = "توصيل لباب المنزل عبر يالدين (70 ألف)"

الإجمالي = سعر_الكتب + shipping_cost
if سعر_الكتب > 0:
    st.write("---")
    st.write(f"**💰 سعر الكتب الإجمالي:** {سعر_الكتب} دج ({int(سعر_الكتب/10)} ألف)")
    st.write(f"**🚚 طريقة الاستلام الحالية:** {shipping_method}")
    st.markdown(f"### 🛑 المبلغ الإجمالي المستحق: **{الإجمالي} دج ({int(الإجمالي/10)} ألف)**")
    st.write("---")
submit_button = st.button("🚀 إرسال الطلب الآن")
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
    msg = (f"<b>🔔 طلبية جديدة في متجر توفيق!</b>\n\n"
           f"━━━━━━━━━━━━━━\n"
           f"👤 <b>الاسم:</b> {name}\n"
           f"📞 <b>الهاتف:</b> {phone}\n"
           f"📍 <b>الولاية:</b> {wilaya}\n"
           f"🚚 <b>طريقة التوصيل:</b> {shipping}\n"
           f"🏠 <b>العنوان:</b> {location}\n"
           f"━━━━━━━━━━━━━━\n"
           f"<i>تم استلام الطلب بنجاح. جهّز الكتاب وتوكل على الله!</i>")
        st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border: 2px dashed #1E3A8A; margin-top: 20px; text-align: right;' dir='rtl'>
            <h3 style='text-align: center; color: #1E3A8A; margin-top: 0;'>🧾 الفاتورة الرسمية للطلب</h3>
            <p><b>👤 الاسم الكامل:</b> {name}</p>
            <p><b>📞 رقم الهاتف:</b> {phone}</p>
            <p><b>📍 العنوان/الولاية:</b> {wilaya}</p>
            <p><b>📚 الكتب المطلوبة:</b> {books_text}</p>
            <hr style='border-top: 1px dashed #9CA3AF;'>
            <p><b>💰 سعر الكتب:</b> {سعر_الكتب} دج ({int(سعر_الكتب/10)} ألف)</p>
            <p><b>🚚 طريقة التوصيل:</b> {shipping_method}</p>
            <h4 style='color: #B91C1C; margin-bottom: 0;'>🛑 المبلغ الإجمالي المستحق: {الإجمالي} دج ({int(الإجمالي/10)} ألف)</h4>
        </div>
        """, unsafe_allow_html=True)
