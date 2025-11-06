"""
saeedforouzandeh: https://github.com/SaeedForouzandeh
برنامه با رابط گرافیکی Tkinter 
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ListOperationsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("سعید فوروزنده")
        self.root.geometry("950x800")
        
        self.colors = {
            'dark_green': '#1a3c34',
            'jade': '#00a86b',
            'gold': '#523d00',
            'light_gold': '#fbf8dc',
            'dark_bg': '#0d1f17',
            'text_light': '#e8f4f0'
        }
        
        self.root.configure(bg=self.colors['dark_bg'])
        
        # تاریخچه عملیات
        self.history = []
        
        # تعریف متغیرهای ورودی
        self.count_entry = None
        self.max_entry = None
        self.reverse_entry = None
        self.main_string_while_entry = None
        self.sub_string_while_entry = None
        self.main_string_for_entry = None
        self.sub_string_for_entry = None
        self.list1_entry = None
        self.list2_entry = None
        self.sort_entry = None
        
        self.setup_gui()
    
    def setup_gui(self):
        # استایل‌ها
        style = ttk.Style()
        
        # تنظیم استایل برای دکمه‌ها
        style.configure('Jade.TButton', 
                       font=('Tahoma', 10, 'bold'), 
                       padding=10,
                       background=self.colors['jade'],
                       foreground='black',
                       borderwidth=2,
                       relief='raised')
        
        style.map('Jade.TButton',
                        background=[('active', self.colors['gold']),
                           ('pressed', self.colors['gold'])],
                 foreground=[('active', 'black'),
                           ('pressed', 'black')])
        
        # تنظیم استایل برای سایر ویجت‌ها
        style.configure('TLabel', 
                       background=self.colors['dark_bg'], 
                       foreground=self.colors['text_light'], 
                       font=('Tahoma', 10))
        
        style.configure('TFrame', 
                       background=self.colors['dark_bg'])
        
        style.configure('TNotebook', 
                       background=self.colors['dark_bg'])
        
        style.configure('TNotebook.Tab', 
                       font=('Tahoma', 9, 'bold'), 
                       padding=10,
                       background=self.colors['dark_green'],
                       foreground=self.colors['gold'])
        
        # هدر
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=15, fill='x')
        
        title_label = tk.Label(header_frame, 
                             text="🧩 سیستم عملیات لیست و رشته", 
                             font=('Tahoma', 18, 'bold'),
                             fg=self.colors['light_gold'], 
                             bg=self.colors['dark_bg'])
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame, 
                                text="توسعه داده شده توسط سعید فوروزنده", 
                                font=('Tahoma', 12),
                                fg=self.colors['jade'], 
                                bg=self.colors['dark_bg'])
        subtitle_label.pack()
        
        # تب‌ها
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=15, pady=10)
        
        # تب‌های مختلف - ۸ تابع
        self.create_count_tab(notebook)           # تابع ۱
        self.create_max_tab(notebook)             # تابع ۲
        self.create_reverse_tab(notebook)         # تابع ۳
        self.create_substring_while_tab(notebook) # تابع ۴-الف
        self.create_substring_for_tab(notebook)   # تابع ۴-ب
        self.create_merge_tab(notebook)           # تابع ۵
        self.create_sort_tab(notebook)            # تابع ۶
        self.create_history_tab(notebook)         # تاریخچه
        
        # پاورقی
        footer_frame = ttk.Frame(self.root)
        footer_frame.pack(fill='x', pady=10)
        
        exit_btn = ttk.Button(footer_frame, text="خروج", command=self.root.quit, style='Jade.TButton')
        exit_btn.pack(side='left', padx=10)
        
        clear_btn = ttk.Button(footer_frame, text="پاک کردن تاریخچه", command=self.clear_history, style='Jade.TButton')
        clear_btn.pack(side='left', padx=10)
    
    def create_count_tab(self, notebook):
        """تابع ۱: شمارش عناصر لیست"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۱. 📊 شمارش عناصر")
        
        self.count_entry = self.create_input_section(frame, "لیست را وارد کنید (با کاما جدا کنید):", "1,2,3,4,5")
        
        ttk.Button(frame, text="شمارش عناصر", 
                  command=self.count_elements, style='Jade.TButton').pack(pady=15)
        
        self.count_result = self.create_result_text(frame)
    
    def create_max_tab(self, notebook):
        """تابع ۲: پیدا کردن بزرگترین عنصر"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۲. 📈 بزرگترین عنصر")
        
        self.max_entry = self.create_input_section(frame, "لیست اعداد را وارد کنید (با کاما جدا کنید):", "5,12,3,8,25,1")
        
        ttk.Button(frame, text="پیدا کردن بزرگترین عنصر", 
                  command=self.find_max_element, style='Jade.TButton').pack(pady=15)
        
        self.max_result = self.create_result_text(frame)
    
    def create_reverse_tab(self, notebook):
        """تابع ۳: معکوس کردن لیست"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۳. 🔄 معکوس کردن")
        
        self.reverse_entry = self.create_input_section(frame, "لیست را وارد کنید (با کاما جدا کنید):", "a,b,c,d,e")
        
        ttk.Button(frame, text="معکوس کردن لیست", 
                  command=self.reverse_list, style='Jade.TButton').pack(pady=15)
        
        self.reverse_result = self.create_result_text(frame)
    
    def create_substring_while_tab(self, notebook):
        """تابع ۴-الف: شمارش زیررشته با while"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۴. 🔍 شمارش با WHILE")
        
        entries = self.create_double_input_section(frame, 
                                       "رشته اصلی:", "python is great, python is powerful, python is easy",
                                       "زیررشته مورد نظر:", "python")
        self.main_string_while_entry, self.sub_string_while_entry = entries
        
        ttk.Button(frame, text="شمارش با حلقه WHILE", 
                  command=self.count_substring_while, style='Jade.TButton').pack(pady=15)
        
        self.substring_while_result = self.create_result_text(frame, height=5)
    
    def create_substring_for_tab(self, notebook):
        """تابع ۴-ب: شمارش زیررشته با for"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۵. 🔍 شمارش با FOR")
        
        entries = self.create_double_input_section(frame, 
                                       "رشته اصلی:", "hello world, hello python, hello programming",
                                       "زیررشته مورد نظر:", "hello")
        self.main_string_for_entry, self.sub_string_for_entry = entries
        
        ttk.Button(frame, text="شمارش با حلقه FOR", 
                  command=self.count_substring_for, style='Jade.TButton').pack(pady=15)
        
        self.substring_for_result = self.create_result_text(frame, height=5)
    
    def create_merge_tab(self, notebook):
        """تابع ۶: ادغام یک در میان دو لیست"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۶. ⚡ ادغام لیست‌ها")
        
        entries = self.create_double_input_section(frame, 
                                       "لیست اول:", "1,3,5,7",
                                       "لیست دوم:", "2,4,6,8,10")
        self.list1_entry, self.list2_entry = entries
        
        ttk.Button(frame, text="ادغام یک در میان", 
                  command=self.merge_alternate, style='Jade.TButton').pack(pady=15)
        
        self.merge_result = self.create_result_text(frame, height=5)
    
    def create_sort_tab(self, notebook):
        """تابع ۷: مرتب‌سازی لیست"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۷. 📊 مرتب‌سازی لیست")
        
        self.sort_entry = self.create_input_section(frame, "لیست اعداد را وارد کنید (با کاما جدا کنید):", "34,12,7,89,3,45,23")
        
        ttk.Button(frame, text="مرتب‌سازی صعودی", 
                  command=self.sort_list, style='Jade.TButton').pack(pady=15)
        
        self.sort_result = self.create_result_text(frame)
    
    def create_history_tab(self, notebook):
        """تب تاریخچه عملیات - تابع ۸"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="۸. 📜 تاریخچه")
        
        tk.Label(frame, text="تاریخچه عملیات:", 
                bg=self.colors['dark_bg'], 
                fg=self.colors['gold'], 
                font=('Tahoma', 12, 'bold')).pack(pady=15)
        
        self.history_text = scrolledtext.ScrolledText(
            frame, 
            height=18, 
            width=85, 
            font=('Tahoma', 9),
            bg=self.colors['dark_green'],
            fg=self.colors['text_light'],
            insertbackground=self.colors['jade']
        )
        self.history_text.pack(pady=10, fill='both', expand=True, padx=10)
    
    def create_input_section(self, parent, label_text, default_value=""):
        """ایجاد بخش ورودی تک خطی"""
        label = tk.Label(parent, text=label_text, 
                       bg=self.colors['dark_bg'], 
                       fg=self.colors['text_light'], 
                       font=('Tahoma', 10))
        label.pack(pady=8)
        
        entry = tk.Entry(parent, width=60, font=('Tahoma', 9),
                        bg='white',
                        fg='black',
                        insertbackground='black')
        entry.pack(pady=5)
        entry.insert(0, default_value)
        
        return entry
    
    def create_double_input_section(self, parent, label1, default1, label2, default2):
        """ایجاد بخش ورودی دوخطی"""
        # ورودی اول
        label1_widget = tk.Label(parent, text=label1, 
                               bg=self.colors['dark_bg'], 
                               fg=self.colors['text_light'], 
                               font=('Tahoma', 10))
        label1_widget.pack(pady=8)
        
        entry1 = tk.Entry(parent, width=60, font=('Tahoma', 9),
                         bg='white',
                         fg='black',
                         insertbackground='black')
        entry1.pack(pady=5)
        entry1.insert(0, default1)
        
        # ورودی دوم
        label2_widget = tk.Label(parent, text=label2, 
                               bg=self.colors['dark_bg'], 
                               fg=self.colors['text_light'], 
                               font=('Tahoma', 10))
        label2_widget.pack(pady=8)
        
        entry2 = tk.Entry(parent, width=60, font=('Tahoma', 9),
                         bg='white',
                         fg='black',
                         insertbackground='black')
        entry2.pack(pady=5)
        entry2.insert(0, default2)
        
        return entry1, entry2
    
    def create_result_text(self, parent, height=4):
        """ایجاد ویجت Text برای نمایش نتایج"""
        text_widget = tk.Text(parent, height=height, width=75, font=('Tahoma', 9),
                             bg=self.colors['dark_green'],
                             fg=self.colors['light_gold'])
        text_widget.pack(pady=10, padx=10)
        return text_widget
    
    def parse_list(self, text):
        """تبدیل رشته به لیست"""
        try:
            if not text:
                return []
                
            elements = [x.strip() for x in text.split(',') if x.strip()]
            if not elements:
                return []
                
            # بررسی آیا همه عناصر عدد هستند
            if all(element.replace('-', '').replace('.', '').isdigit() for element in elements):
                return [float(element) if '.' in element else int(element) for element in elements]
            else:
                return elements
        except Exception as e:
            print(f"خطا در تبدیل لیست: {e}")
            return []
    
    # تابع ۱: شمارش عناصر لیست
    def count_elements(self):
        """تابع ۱: شمارش عناصر لیست"""
        try:
            if not self.count_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            text = self.count_entry.get()
            lst = self.parse_list(text)
            
            count = len(lst)
            result = f"📊 نتایج شمارش عناصر:\n"
            result += f"لیست وارد شده: {lst}\n"
            result += f"تعداد عناصر: {count}\n"
            if lst:
                result += f"نوع داده: {'اعداد' if all(isinstance(x, (int, float)) for x in lst) else 'رشته‌ها'}"
            else:
                result += f"لیست خالی است"
            
            self.count_result.delete(1.0, tk.END)
            self.count_result.insert(1.0, result)
            
            self.history.append(f"شمارش عناصر: {lst} → {count} عنصر")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    # تابع ۲: پیدا کردن بزرگترین عنصر
    def find_max_element(self):
        """تابع ۲: پیدا کردن بزرگترین عنصر"""
        try:
            if not self.max_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            text = self.max_entry.get()
            lst = self.parse_list(text)
            
            if not lst:
                messagebox.showwarning("هشدار", "لیست خالی است!")
                return
            
            # بررسی اینکه آیا همه عناصر عددی هستند
            if not all(isinstance(x, (int, float)) for x in lst):
                messagebox.showwarning("هشدار", "لیست باید شامل اعداد باشد!")
                return
            
            max_element = max(lst)
            max_index = lst.index(max_element)
            
            result = f"📈 نتایج پیدا کردن بزرگترین عنصر:\n"
            result += f"لیست: {lst}\n"
            result += f"بزرگترین عنصر: {max_element}\n"
            result += f"موقعیت در لیست: ایندکس {max_index}"
            
            self.max_result.delete(1.0, tk.END)
            self.max_result.insert(1.0, result)
            
            self.history.append(f"بزرگترین عنصر: {lst} → {max_element}")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    # تابع ۳: معکوس کردن لیست
    def reverse_list(self):
        """تابع ۳: معکوس کردن لیست"""
        try:
            if not self.reverse_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            text = self.reverse_entry.get()
            lst = self.parse_list(text)
            
            original = lst.copy()
            reversed_lst = lst[::-1]
            
            result = f"🔄 نتایج معکوس کردن:\n"
            result += f"لیست اصلی: {original}\n"
            result += f"لیست معکوس: {reversed_lst}"
            
            self.reverse_result.delete(1.0, tk.END)
            self.reverse_result.insert(1.0, result)
            
            self.history.append(f"معکوس کردن: {original} → {reversed_lst}")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    # تابع ۴-الف: شمارش زیررشته با while
    def count_substring_while(self):
        """تابع ۴-الف: شمارش زیررشته با حلقه while"""
        try:
            if not self.main_string_while_entry or not self.sub_string_while_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            main_string = self.main_string_while_entry.get()
            sub_string = self.sub_string_while_entry.get()
            
            if not main_string or not sub_string:
                messagebox.showwarning("هشدار", "هر دو رشته باید پر باشند!")
                return
            
            count = 0
            index = 0
            sub_length = len(sub_string)
            
            # حلقه while برای شمارش
            while index < len(main_string):
                found_index = main_string.find(sub_string, index)
                if found_index == -1:
                    break
                count += 1
                index = found_index + 1
            
            result = f"🔍 نتایج شمارش با حلقه WHILE:\n"
            result += f"رشته اصلی: '{main_string}'\n"
            result += f"زیررشته: '{sub_string}'\n"
            result += f"تعداد تکرار: {count} بار\n"
            
            self.substring_while_result.delete(1.0, tk.END)
            self.substring_while_result.insert(1.0, result)
            
            self.history.append(f"شمارش با WHILE: '{sub_string}' → {count} بار")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    # تابع ۴-ب: شمارش زیررشته با for
    def count_substring_for(self):
        """تابع ۴-ب: شمارش زیررشته با حلقه for"""
        try:
            if not self.main_string_for_entry or not self.sub_string_for_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            main_string = self.main_string_for_entry.get()
            sub_string = self.sub_string_for_entry.get()
            
            if not main_string or not sub_string:
                messagebox.showwarning("هشدار", "هر دو رشته باید پر باشند!")
                return
            
            count = 0
            sub_length = len(sub_string)
            
            # حلقه for برای شمارش
            for i in range(len(main_string) - sub_length + 1):
                if main_string[i:i + sub_length] == sub_string:
                    count += 1
            
            result = f"🔍 نتایج شمارش با حلقه FOR:\n"
            result += f"رشته اصلی: '{main_string}'\n"
            result += f"زیررشته: '{sub_string}'\n"
            result += f"تعداد تکرار: {count} بار\n"
            
            self.substring_for_result.delete(1.0, tk.END)
            self.substring_for_result.insert(1.0, result)
            
            self.history.append(f"شمارش با FOR: '{sub_string}' → {count} بار")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    # تابع ۶: ادغام یک در میان دو لیست
    def merge_alternate(self):
        """تابع ۶: ادغام یک در میان دو لیست"""
        try:
            if not self.list1_entry or not self.list2_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            list1 = self.parse_list(self.list1_entry.get())
            list2 = self.parse_list(self.list2_entry.get())
            
            merged_list = []
            max_length = max(len(list1), len(list2))
            
            for i in range(max_length):
                if i < len(list1):
                    merged_list.append(list1[i])
                if i < len(list2):
                    merged_list.append(list2[i])
            
            result = f"⚡ نتایج ادغام یک در میان:\n"
            result += f"لیست اول ({len(list1)} عنصر): {list1}\n"
            result += f"لیست دوم ({len(list2)} عنصر): {list2}\n"
            result += f"لیست ادغام شده ({len(merged_list)} عنصر): {merged_list}"
            
            self.merge_result.delete(1.0, tk.END)
            self.merge_result.insert(1.0, result)
            
            self.history.append(f"ادغام: {list1} + {list2} → {merged_list}")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    # تابع ۷: مرتب‌سازی لیست
    def sort_list(self):
        """تابع ۷: مرتب‌سازی لیست"""
        try:
            if not self.sort_entry:
                messagebox.showerror("خطا", "ویجت ورودی پیدا نشد!")
                return
                
            text = self.sort_entry.get()
            lst = self.parse_list(text)
            
            if not lst:
                messagebox.showwarning("هشدار", "لیست خالی است!")
                return
            
            if not all(isinstance(x, (int, float)) for x in lst):
                messagebox.showwarning("هشدار", "لیست باید شامل اعداد باشد!")
                return
            
            original = lst.copy()
            sorted_lst = sorted(lst)
            
            result = f"📊 نتایج مرتب‌سازی:\n"
            result += f"لیست اصلی: {original}\n"
            result += f"لیست مرتب شده: {sorted_lst}\n"
            result += f"تعداد عناصر: {len(lst)}"
            
            self.sort_result.delete(1.0, tk.END)
            self.sort_result.insert(1.0, result)
            
            self.history.append(f"مرتب‌سازی: {original} → {sorted_lst}")
            self.update_history()
            
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در پردازش: {str(e)}")
    
    def update_history(self):
        """بروزرسانی تاریخچه"""
        self.history_text.delete(1.0, tk.END)
        if not self.history:
            self.history_text.insert(tk.END, "📭 تاریخچه عملیات خالی است\n")
            return
            
        for i, operation in enumerate(self.history, 1):
            self.history_text.insert(tk.END, f"{i}. {operation}\n")
            self.history_text.insert(tk.END, "─" * 60 + "\n")
    
    def clear_history(self):
        """پاک کردن تاریخچه"""
        self.history.clear()
        self.history_text.delete(1.0, tk.END)
        messagebox.showinfo("موفق", "تاریخچه پاک شد!")

def main():
    """تابع اصلی"""
    try:
        root = tk.Tk()
        app = ListOperationsGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"خطا در اجرای برنامه: {e}")
        input("برای خروج Enter بزنید...")

if __name__ == "__main__":
    main()