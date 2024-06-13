#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


class Circle(object):
    
    
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
  
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
   
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 


# In[3]:


RedCircle = Circle(10, 'red')


# In[4]:


dir(RedCircle)


# In[5]:


RedCircle.radius


# In[6]:


RedCircle.color


# In[7]:


RedCircle.radius = 1
RedCircle.radius


# In[8]:


RedCircle.drawCircle()


# In[9]:


print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)


# In[10]:


BlueCircle = Circle(radius=100)


# In[11]:


BlueCircle.radius


# In[12]:


BlueCircle.color


# In[13]:


BlueCircle.drawCircle()


# In[ ]:




