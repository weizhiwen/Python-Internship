"""
2.设计一个书籍信息管理系统
- 1.用户信息包含：用户编号，用户名，密码，邮箱
- 2.书籍信息包含：书籍类型、书籍编号，书籍名称、书籍价格
- 3.用户注册，注册时输入用户名、密码、邮箱，编号自动生成
- 4.系统登录，对用户名、密码进行校验，只有3次登录机会
- 5.登录成功后，显示如下菜单：
  - 1.根据书籍类型查看书籍：先选择书籍类型，再根据所选类型显示对应类型的书籍信息
  - 2.查看所有书籍信息：
  - 3.更新书籍信息：更新书籍名称与价格
  - 4.删除书籍：根据书籍编号删除
  - 5.扩展：为书籍信息展示添加分页(上一页、下一页)。
"""

# 用户信息类
class User:
  def __init__(self, name, password, id=None,email=None):
      self.name = name
      self.password = password
      self.id = id
      self.email = email
  def __repr__(self):
      return "id:{}, name: {}, password: {}, email: {}".format(self.id, self.name, self.password, self.email)

# 书籍信息类
class Book:
    def __init__(self, type, id, name, price):
        self.type = type
        self.id = id
        self.name = name
        self.price = price
    def __repr__(self):
        return "type:{}, id:{}, name: {}, price: {}".format(self.type, self.id, self.name, self.price)

# 系统主页面
def index():
    print("书籍信息管理系统\n"
          "1.注册, 2.登录, 0.退出")
    while True:
        choice =  input("请输入您的选项：")
        if choice == "1":
            # 注册页面及处理
            user = register()
            print("注册填写的信息为", user)
            doRegister(userDict, user)
        elif choice == "2":
            # 登录页面及处理
            i = 3
            while i > 0:
                user = login()
                print("登录的用户信息为", user)
                flag = doLogin(userDict, user)
                if flag:
                    print("登录成功！")
                    manageBook()
                else:
                    i -= 1
                    print("登录失败，还剩 %d 次机会" %i)
            print("3 次登录机会已用完！")
        elif choice == "0":
            break
        else:
            print("输入不符合要求")

# 用户注册页面
def register():
    print("请输入注册信息")
    name = input("用戶名：")
    password = input("密码：")
    email = input("邮箱：")
    return User(name, password, email)

# 注册用户处理
def doRegister(userDict, user):
    id = len(userDict)
    user.id = id
    userDict[str(id)] = user  # 添加用户信息到字典中
    print("注册成功！")
    for key in userDict.keys():
        print(key + ': ' + str(userDict[key]))

# 用户登录页面
def login():
    print("请填写下面信息")
    name = input("用户名：")
    password = input("密码：")
    return User(name, password)

# 用户登录处理
def doLogin(userDict, user):
    for value in userDict.values():
        if value.name == user.name and value.password == user.password:
            return True
    return False

# 图书管理页面
def manageBook():
    print("欢迎使用！")
    print("1.根据书籍类型查看书籍\n"
          "2.查看所有书籍信息\n"
          "3.更新书籍信息：更新书籍名称与价格\n"
          "4.删除书籍：根据书籍编号删除\n"
          "0.退出")
    while True:
        choice = input("请输入您的选项：")
        if choice == "1":
            type = input("请输入要查看的书籍类型：")
            selectByType(bookDict, type)
        elif choice == "2":
            selectAll(bookDict)
        elif choice == "3":
            id = input("请输入要更新的书籍编号：")
            updateById(bookDict, id)
        elif choice == "4":
            id = input("请输入要删除的书籍编号：")
            deleteById(bookDict, id)
        elif choice == "0":
            break
        else:
            print("输入不符合要求")

# 根据书籍类型查询书籍信息
def selectByType(bookDict, type):
    for value in bookDict.values():
        if value.type == type:
            print(value)

# 查询所有书籍信息
def selectAll(bookDict):
    # 为书籍信息展示添加分页(上一页、下一页)
    currentPage = 1  # 当前页数
    countPerPage = 2  # 每页条数
    totalCount = len(bookDict)  # 书籍总条数
    totalPages = int((totalCount / countPerPage))  # 书籍总页数
    # 字典转列表
    bookList = []
    for value in bookDict.values():
        bookList.append(value)
    print("字典转换后的列表为", bookList)
    print("当前为第 %d 页" %currentPage)
    index = (currentPage - 1) * countPerPage
    for book in bookList[index:index + countPerPage]:
        print(book)
    print("-1.上一页\n"
          "1.下一页\n"
          "0.退出")
    while True:
        choice = input("请输入您的选项：")
        if choice == "-1":
            if currentPage <= 1:
                print("没有上一页")
            else:
                currentPage -= 1
                index = (currentPage - 1) * countPerPage
                print("当前为 %d 页" % currentPage)
                for book in bookList[index:index + countPerPage]:
                    print(book)
        elif choice == "1":
            if currentPage >= totalPages:
                print("没有下一页")
            else:
                currentPage += 1
                index = (currentPage - 1) * countPerPage
                print("当前为 %d 页" % currentPage)
                for book in bookList[index:index + countPerPage]:
                    print(book)
        elif choice == "0":
            break
        else:
            print("输入不符合要求")

# 根据编号修改书籍
def updateById(bookDict, id):
    name = input("请输入要更新书籍名称：")
    bookDict[id].name = name
    price = input("请输入要更新书籍价格：")
    bookDict[id].price = price
    print("更新后的书籍为", bookDict[id])

# 根据编号删除书籍
def deleteById(bookDict, id):
    del bookDict[id]

if __name__ == "__main__":
    user = User("admin", "admin", "0", "weizhiwen23@gmail.com")
    userDict = {}  # 用户信息字典
    userDict["0"] = user
    # 打印用户信息
    # for key in userDict.keys():
    #     print(key + ":" + str(userDict[key]))
    # 准备数据
    book1 = Book("Python", "1", "《Python快速入门》", "10.0")
    book2 = Book("Python", "2", "《Python入门到进阶》", "20.0")
    book3 = Book("Java", "3", "《Java快速入门》", "10.0")
    book4 = Book("Java", "4", "《Java入门到进阶》", "20.0")
    book5 = Book("C语言", "5", "《C语言快速入门》", "10.0")
    book6 = Book("C语言", "6", "《C语言入门到进阶》", "20.0")
    bookDict = {}  # 书籍信息字典
    bookDict["1"] = book1
    bookDict["2"] = book2
    bookDict["3"] = book3
    bookDict["4"] = book4
    bookDict["5"] = book5
    bookDict["6"] = book6
    # print("打印书籍信息：")
    # for key in bookDict.keys():
    #     print(key + ':' + str(bookDict[key]))
    index()