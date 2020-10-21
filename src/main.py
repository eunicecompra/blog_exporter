from src import website

website.launch("http://inanywhereelse.blogspot.com/")
website.toggle_posts()
blog_posts = website.list_posts()
website.save_as_pdf(blog_posts)
website.close()
