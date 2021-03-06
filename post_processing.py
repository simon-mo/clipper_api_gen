
# coding: utf-8

# Clipper API Doc Post Processing Script
# 
# Precondition:
# - There exists public/index.html generated by spectable already
# - There exists clipper_style.html with modification
# 
# Task:
# - This script add clipper_style to header of index.html
# - This script cleaned the word "undefined"
# - This script save the new html as `clipper_index.html`

# In[25]:


from bs4 import BeautifulSoup


# In[26]:


html_doc = open('public/index.html','r').read()
clipper_style = open('clipper_style.html','r').read()


# In[27]:


soup = BeautifulSoup(html_doc, 'html.parser')
style_to_add = BeautifulSoup(clipper_style, 'html.parser')


# In[28]:


head = soup.find('head')
last_script = head.find_all('script')[-1]
last_script.insert_after(style_to_add)


# In[36]:


cleaned = soup.prettify().replace('undefined','')


# In[37]:


with open('public/clipper_index.html','w') as f:
    f.write(cleaned)
    f.flush()

