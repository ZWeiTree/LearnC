import json
import os

file_name_books = "book.json"
file_name_users = "user.json"


# main menu
def menu():
    print('·' * 40)
    print('请选择：')
    print("1: 注册：")
    print("2. 登陆：")
    print("3. 退出")


# user
def user_menu(self):
    print('·' * 40)
    print('%s 登录成功' % self)
    print('1. 添加单本')
    print('2. 删除单本')
    print('3. 修改单本')
    print('4. 查询单本')
    print('5. 查询全部')
    print('6. 退出')


class Operator:
    identity = ''
    user_name = ''
    password = ''


class Book:
    book_name = ''
    book_price = ''
    book_author = ''


# administrator
def administrator():
    print('·' * 40)
    print('管理员登陆成功')
    print('1. 删除用户')
    print('2. 修改用户名')
    print('3. 查询用户')
    print('4. 查询全部')
    print('5. 退出')


# delete user
def del_user():
    user_name = input('要删除的用户：')
    count = 0
    index = 0
    for i in users:
        if user_name == i['name']:
            count = 1
            del users[index]
            print('#' * 40)
            print('已删除')
        index += 1
    if count == 0:
        print('#' * 40)
        print('无用户')


# edit user
def edit_user():
    user_name = input('要修改的用户：')
    count = 0
    index = 0
    for i in users:
        if user_name == i['name']:
            count = 1
            del users[index]
            new_user_name = input('新用户名：')
            new_user_password = input('新密码：')
            new_user = {'name': new_user_name, 'password': new_user_password}
            users.append(new_user)
            print('修改成功')
        index += 1
    if count == 0:
        print('无用户')


# query one user
def look_user():
    user_name = input('要查询的用户：')
    count = 0
    print('*用户名\t*密码\t')
    for i in users:
        if user_name == i['name']:
            count = 1
            print('%s\t\t%s\t' % (i['name'], i['password']))
    if count == 0:
        print('#'*40)
        print('无用户')


# all users
def look_users():
    print('*用户名\t*密码\t')
    for i in users:
        print('%s\t\t%s\t' % (i['name'], i['password']))


# sign up
def sign_up():
    user_name = input("用户名：")
    for i in users:
        if user_name == i['name']:
            print('#' * 40)
            print("不可用")
            return
    user_password = input("密码：")
    user = {'name': user_name, 'password': user_password}
    users.append(user)
    print('#' * 40)
    print("注册成功")


# sign in
def login():
    user_name = input("用户名：")
    user_password = input("密码：")
    count = 0
    for i in users:
        if user_name == i['name']:
            count = 1
            if user_password == i['password']:
                print('#' * 40)
                print("登陆成功")
                return user_name
            else:
                print('#' * 40)
                print("密码错误")
    if count == 0:
        print('#'*40)
        print("无用户")


# add
def add_book():
    book_name = input('要添加的书名：')
    for i in books:
        if book_name == i['name']:
            print('#' * 40)
            print("已存在")
            return
    book_author = input('作者:')
    book_price = input('价格：')
    book = {'name': book_name, 'author': book_author, 'price': book_price}
    books.append(book)
    print('#' * 40)
    print('添加成功')


# delete
def del_book():
    book_name = input('要删除书名：')
    count = 0
    index = 0
    for i in books:
        if book_name == i['name']:
            count = 1
            del books[index]
            print('#' * 40)
            print('删除成功')
        index += 1
    if count == 0:
        print('#'*40)
        print('查无此书')


# edit book
def edit_book():
    book_name = input('要修改书名：')
    count = 0
    index = 0
    for i in books:
        if book_name == i['name']:
            count = 1
            del books[index]
            new_book_name = input('新书名：')
            new_book_author = input('作者：')
            new_book_price = input('价格：')
            new_book = {'name': new_book_name, 'author': new_book_author, 'price': new_book_price}
            books.append(new_book)
            print('#' * 40)
            print('修改成功')
        index += 1
    if count == 0:
        print('#'*40)
        print('查无此书')


# query one book
def look_book():
    book_name = input('要查询书名：')
    count = 0
    print('*书名\t\t*作者\t\t*价格\t')
    for i in books:
        if book_name == i['name']:
            count = 1
            print('%s\t%s\t%s\t' % (i['name'], i['author'], i['price']))
    if count == 0:
        print('#'*40)
        print('查无此书')


# all books
def look_books():
    print('*书名\t\t*作者\t\t*价格\t')
    for i in books:
        print('[%s]\t%s\t%s\t' % (i['name'], i['author'], i['price']))


# initial
def get_init_data():
    if (not os.path.exists(file_name_users)) | (not os.path.exists(file_name_books)):
        raise print("缺少必要文件：", file_name_books, file_name_users)
    with open(file_name_books, 'r', encoding='utf-8') as f:
        books_json = json.load(f)
    with open(file_name_users, 'r', encoding='utf-8') as f:
        users_json = json.load(f)
    return books_json, users_json


# update
def set_init_data():
    with open(file_name_books, 'w', encoding='utf-8') as f:
        f.write(json.dumps(books, ensure_ascii=False, indent=4))
    with open(file_name_users, 'w', encoding='utf-8') as f:
        f.write(json.dumps(users, ensure_ascii=False, indent=4))


# user & administrator
def while_user(name):
    while name:
        # administrator is Admin
        if name == 'admin':
            administrator()
            administrator_n = input()
            if administrator_n == '1':
                del_user()
            elif administrator_n == '2':
                edit_user()
            elif administrator_n == '3':
                look_user()
            elif administrator_n == '4':
                look_users()
            elif administrator_n == '5':
                break
            else:
                print('#' * 40)
                print("ERROR")
                print("重新选择：")

        else:
            user_menu(name)
            user_n = input()
            if user_n == '1':
                add_book()
            elif user_n == '2':
                del_book()
            elif user_n == '3':
                edit_book()
            elif user_n == '4':
                look_book()
            elif user_n == '5':
                look_books()
            elif user_n == '6':
                break
            else:
                print('#' * 40)
                print("ERROR")
                print("重新选择：")


# main
def main():
    while True:
        menu()
        menu_n = input()
        if menu_n == '1':
            sign_up()
        elif menu_n == '2':
            name = login()

            while_user(name)

        elif menu_n == '3':
            set_init_data()
            break
        else:
            print('#' * 40)
            print("ERROR")
            print("重新选择：")


if __name__ == '__main__':
    books, users = get_init_data()

    main()
