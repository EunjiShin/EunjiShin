import feedparser, datetime

tistory_blog_uri="https://hogwart-scholars.tistory.com/" #Your blog address here
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:e0c3fc,100:a6c1ee&height=300&section=header&text=Woody's%20github&fontSize=90&fontColor=FFFFFF)
### ✨ 최적화 하는 개발자 신은지

</br>

 ### 🌱 Info 
Email: sej.gm3@gmail.com </br>
Blog : https://hogwart-scholars.tistory.com/ </br>
Second Blog : https://velog.io/@ej_shin 

</br>

### 🛠 Tech 
<p align="center">
<div style="display: flex; align-items: flex-start;">
<img src="https://techstack-generator.vercel.app/java-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/js-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/ts-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="80" height="80" />
</div> </br>
<div style="display: flex; align-items: flex-start;">
<img src="https://techstack-generator.vercel.app/restapi-icon.svg" alt="icon" width="80" height="80" />
<img src="https://user-images.githubusercontent.com/38103085/181780616-1a299b1f-990a-468b-b708-dec753ba7851.png" alt="spring-boot" wide="70" height="70">
<img src="https://user-images.githubusercontent.com/38103085/201467463-63243cca-c2b4-4fef-8370-1e9327c50c84.svg" alt= "nest-js" wide="80" height="80">
<img src="https://techstack-generator.vercel.app/django-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/graphql-icon.svg" alt="icon" width="80" height="80" />
</div> </br>
<div style="display: flex; align-items: flex-start;">
<img src="https://techstack-generator.vercel.app/mysql-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/aws-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/docker-icon.svg" alt="icon" width="80" height="80" />
<img src="https://techstack-generator.vercel.app/github-icon.svg" alt="icon" width="80" height="80" />
</div>
<sub>created by <a href="https://github.com/qkrdmstlr3/techstack-generator" target="_blank">https://github.com/qkrdmstlr3/techstack-generator</a>
</sub>  
</p>

</br></br>

![EunjiShin's GitHub stats](https://github-readme-stats.vercel.app/api?username=EunjiShin&show_icons=true&theme=buefy)

</br></br>

## Recent blog posts

</div>
""" # list of blog posts will be appended here

lst = []


for i in feed['entries'][:5]:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
