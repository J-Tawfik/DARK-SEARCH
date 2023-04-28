import os
import tkinter as tk
import atexit

#create window
# إنشاء نافذة
window = tk.Tk()
# window title
# إعداد عنوان للنافذة
window.title(" dark search  script demo ")
# window setting
# إعداد حجم النافذة
window.geometry("400x200")

# إضافة عنصر واجهة رسومية (على سبيل المثال، علامة نصية)
label = tk.Label(window, text="welcome to dark search  files demo  this project gui  under devloping  press close to start searching ")
label.pack()  # لإظهار العنصر في النافذة

# دالة للتعامل مع زر الإغلاق
def close_app():
    window.destroy()

# إضافة زر إغلاق
button = tk.Button(window, text="close", command=close_app)
button.pack()

# بدء دورة الحدث الرئيسية
window.mainloop()

def search_file(filename, search_directory):
    """بحث عن ملف باستخدام اسم الملف كمدخل من المستخدم."""

    results = []
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if filename in file:
                # إذا كان اسم الملف موجود في اسم الملف الحالي
                # فإنه يتم إضافته إلى النتائج
                results.append(os.path.join(root, file))

    return results
#file name and directory 
# استخراج اسم الملف ومسار البحث من المستخدم
filename = input("type here to search: ")
search_directory = input(" please enter  search directory (you can let it empty): ")
#search file
# قم بالبحث عن الملف
results = search_file(filename, search_directory)
# print result
# طباعة النتائج
if results:
    print("تم العثور على الملفات التالية:")
    for file in results:
        print(file)
        
else:
    print(" No file was found please try again with another name or directory or try the ultimate version ")


def exit_handler():
    input("Press Enter to exit...")

# تسجيل الدالة كدالة ختامية
#Register the function as an end function
atexit.register(exit_handler)