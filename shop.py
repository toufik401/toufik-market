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
    except Exception as e:
        st.error(f"خطأ في إرسال التليغرام: {e}")
st.title("--- متجر لاقتناء كتاب توفيق للرياضيات ---")
st.write("مرحباً بك في المتجر الإلكتروني، يرجى ملء معلوماتك لطلب الكتب.")
book_price = 400
name = st.text_input("ادخل اسمك كامل:")
phone = st.text_input("ادخل رقم هاتفك:")
wilaya = st.text_input("ادخل ولايتك (مثال: أفلو أو الأغواط):")
shipping_cost = 0
shipping_method = ""
if wilaya == "أفلو":
    delivery = st.radio("هل تريد ميزة التوصيل إلى باب المنزل في أفلو بـ 10 آلاف (100 دج)؟", ("لا، سأستلمه شخصياً مجاناً", "نعم، أريد التوصيل للمنزل"))
     if "نعم" in delivery:
        address = st.text_input("أدخل موقع منزلك في أفلو بالتفصيل:")
        shipping_cost = 100
        shipping_method = "توصيل منزلي في أفلو (100 دج)"
    else:
        shipping_cost = 0
        shipping_method = "استلام شخصي في أفلو (مجاني)"
elif wilaya: 
    st.info("التوصيل المتوفر لولايتك هو عبر شركة يالدين (Yalidine).")
    yalidine_type = st.radio("هل تريد التوصيل إلى (مكتب يالدين) أم (باب المنزل)؟", ("مكتب يالدين", "باب المنزل"))
    
    if yalidine_type == "باب المنزل":
        shipping_cost = 700
        shipping_method = "يالدين - إلى باب المنزل (700 دج)"
    else:
        shipping_cost = 400
        shipping_method = "يالدين - استلام من المكتب (400 دج)"


st.subheader("📖 اختر الكتب بالنقر على المربعات حذاها:")
selected_books = []

if st.checkbox("⬜ كتاب الدوال (400 دج)"):
    selected_books.append("كتاب الدوال")
if st.checkbox("⬜ كتاب المتتاليات (400 دج)"):
    selected_books.append("كتاب المتتاليات")
if st.checkbox("⬜ كتاب الاحتمالات (400 دج)"):
    selected_books.append("كتاب الاحتمالات")
if st.checkbox("⬜ كتاب الأعداد المركبة (400 دج)"):
    selected_books.append("كتاب الأعداد المركبة")
quantity = st.number_input("كم عدد النسخ التي تريد طلبها من الكتب المختارة؟", min_value=1, value=1, step=1)
if st.button("تأكيد وإرسال الطلب 🚀"):
    if not name or not phone or not wilaya:
        st.error("رجاءً عمر كامل معلوماتك (الاسم، الهاتف، والولاية) أولاً!")
    elif not selected_books:
        st.error("يرجى اختيار كتاب واحد على الأقل من المربعات في الأعلى!")
    else:
        total_books_price = len(selected_books) * book_price * quantity
        total_price = total_books_price + shipping_cost
        order_number = random.randint(1000, 9999)
        books_str = ", ".join(selected_books)
        with open("orders.txt", "a", encoding="utf-8") as file:
            file.write(f"رقم الطلب: #{order_number} | الاسم: {name} | الهاتف: {phone} | الولاية: {wilaya} | الكتب: {books_str} (الكمية الإجمالية: {quantity}) | الشحن: {shipping_method} | السعر الإجمالي: {total_price} دج\n")
            file.write("--------------------------------------------------------------------------------\n")
        telegram_message = (
            f"🔔 *طلب جديد واصل يا توفيق!* 🔔\n\n"
            f"📦 *رقم الطلب:* #{order_number}\n"
            f"👤 *الزبون:* {name}\n"
            f"📞 *رقم الهاتف:* `{phone}`\n"
            f"📍 *الولاية:* {wilaya}\n"
            f"📖 *الكتب:* {books_str} (الكمية: {quantity})\n"
            f"🚚 *الشحن:* {shipping_method}\n"
            f"💰 *المبلغ الإجمالي:* {total_price} دج"
        )
        send_telegram_notification(telegram_message)
        st.success(f"✅ تم إرسال طلبك بنجاح يا {name}!")
        st.balloons()
        st.subheader("--- تفاصيل الفاتورة تع طلبك ---")
        st.write(f"**رقم الطلب الخاص بك:** #{order_number}")
        st.write(f"**الكتب المطلوبة:** {books_str}")
        st.write(f"**الكمية الإجمالية:** {quantity} نسخ.")
        st.write(f"**سعر الكتب الإجمالي:** {total_books_price} دج.")
        st.write(f"**سعر الشحن:** {shipping_cost} دج.")
        st.write(f"### 💰 السعر الإجمالي للدفع عند الاستلام: {total_price} دج.")
        st.write("----------------------------------------")
        st.info("شكرًا لثقتك في متجرنا، سنتصل بك قريبًا لتأكيد الشحن.")
