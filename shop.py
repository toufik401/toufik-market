TELEGRAM_TOKEN = "8966476087:AAFFcvYyi6eOh37KDr8vDZ_BiJJU4dI7uDA"
TELEGRAM_CHAT_ID = "8966476087"
def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
>> print("---متجر لاقتناء كتاب توفيق لرياضيات---")
---متجر قتناء كتاب توفيق لرياضيات---
book_price = 400
>>> name = input("ادخل اسمك: ")
ادخل اسمك: 
>>> phone = input("ادخل رقم هاتفك: ")
ادخل رقم هاتفك:
>>> wilaya = input("ادخل ولايتك: ")
ادخل ولايتك: 
>>>if wilaya == "أفلو":
    delivery = input("هل تريد ميزة التوصيل إلى باب المنزل في أفلو بـ 10 آلاف؟ (نعم / لا): ")
    if delivery == "نعم":
        address = input("أدخل موقع منزلك في أفلو بالتفصيل: ")
        shipping_cost = 100  "# هنا رجعناها 100 دج (10 آلاف)"
        print("طريقة الشحن: توصيل منزلي في أفلو (100 دج).")
    else:
        shipping_cost = 0  "# إذا ما حبش التوصيل يجي يرفده باطل"
        print("طريقة الشحن: استلام شخصي (مجاني).")
else:
    print("التوصيل المتوفر لولايتك هو عبر شركة يالدين (Yalidine).")
    yalidine_type = input("هل تريد التوصيل إلى (مكتب يالدين) أم (باب المنزل)؟ ")
    
    if yalidine_type == "باب المنزل":
        shipping_cost = 700
    else:
        shipping_cost = 400  "للمكتب:"
    print(f"طريقة الشحن: عبر يالدين (تكلفة الشحن: {shipping_cost} دج).")
print("\n--- الكتب المتوفرة في المتجر (السعر: 400 دج للكتاب) ---")
print("1. كتاب الدوال")
print("2. كتاب المتتاليات")
print("3. كتاب الاحتمالات")
print("4. كتاب الأعداد المركبة")
book_choice = input("أدخل رقم الكتاب الذي تريد شراءه (1 أو 2 أو 3 أو 4): ")
quantity = int(input("كم عدد الكتب التي تريد طلبها من هذا النوع؟ "))
st.subheader("📖 اختر الكتب بالنقير على المربعات حذاها:")
selected_books = []
if st.checkbox("⬜ كتاب الدوال (400 دج)"):
    selected_books.append("كتاب الدوال")
if st.checkbox("⬜ كتاب المتتاليات (400 دج)"):
    selected_books.append("كتاب المتتاليات")
if st.checkbox("⬜ كتاب الاحتمالات (400 دج)"):
    selected_books.append("كتاب الاحتمالات")
if st.checkbox("⬜ كتاب الأعداد المركبة (400 دج)"):
    selected_books.append("كتاب الأعداد المركبة")
 total_books_price = quantity * book_price 
total_price = total_books_price + shipping_cost   
print("\n----------------------------------------")
print(f"✅ تم إرسال طلبك بنجاح يا {name}!")
order_number = random.randint(1000, 9999) 
print(f"رقم الطلب الخاص بك هو: #{order_number}")
with open("orders.txt", "a", encoding="utf-8") as file:
            books_str = ", ".join(selected_books) 
            file.write(f"رقم الطلب: #{order_number} | الاسم: {name} | الهاتف: {phone} | الولاية: {wilaya} | الكتب: {books_str} (الكمية: {quantity}) | الشحن: {shipping_method} | السعر الإجمالي: {total_price} دج\n")
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
print("--- تفاصيل الفاتورة ---")
print(f"الكتاب المطلوب: {book_name}")
print(f"الكمية: {quantity} كتاب.")
print(f"سعر الكتب الإجمالي: {total_books_price} دج.")
print(f"سعر الشحن: {shipping_cost} دج.")
print(f"💰 السعر الإجمالي للدفع عند الاستلام: {total_price} دج.")
print("----------------------------------------")
print("شكرًا لثقتك في متجرنا، سنتصل بك قريبًا لتأكيد الشحن.")
print("----------------------------------------")

