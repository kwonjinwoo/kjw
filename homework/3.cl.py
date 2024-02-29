# 1 Member 클래스와 Post 클래스를 정의하세요
class Member:
    # 2 Member 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # 3 Member 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"게시물 제목: {self.title}, 게시물 내용: {
            self.content}, 작성자: {self.author.username}")


members = []
animal1 = Member('dog', '강아지', '1591')
animal2 = Member('hamster', '햄스터', '1592')
animal3 = Member('elephant', '코끼리', '1593')

members.append(animal1)
members.append(animal2)
members.append(animal3)

for animal in members:
    print(animal.name)

posts = []
animal1_post1 = Post(title='강아지짤', content='몽글', author=animal1.username)
animal1_post2 = Post(title='강아지짤', content='시바견', author=animal1.username)
animal1_post3 = Post(title='강아지짤', content='불독', author=animal1.username)

posts.append(animal1_post1)
posts.append(animal1_post2)
posts.append(animal1_post3)

animal2_post1 = Post(title='햄스터짤', content='캠벨 햄스터', author=animal2.username)
animal2_post2 = Post(title='햄스터짤', content='골든 햄스터', author=animal2.username)
animal2_post3 = Post(title='햄스터짤', content='윈터 햄스터', author=animal2.username)

posts.append(animal2_post1)
posts.append(animal2_post2)
posts.append(animal2_post3)

animal3_post1 = Post(title='코끼리짤', content='아프리카 코끼리', author=animal3.username)
animal3_post2 = Post(title='코끼리짤', content='아시아 코끼리', author=animal3.username)
animal3_post3 = Post(title='코끼리짤', content='둥근귀 코끼리', author=animal3.username)

posts.append(animal3_post1)
posts.append(animal3_post2)
posts.append(animal3_post3)

for post in posts:
    if "강아지" == post.author:
        print(post.title)
print('')
for post in posts:
    if "아프리카" in post.content:
        print(post.title)
