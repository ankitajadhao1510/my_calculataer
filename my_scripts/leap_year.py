#!/usr/bin/env python
# coding: utf-8

# In[2]:


year= int(input('Which year do you want to check?  '))
if year%4==0:
    if year%100:
        if year%400:
            print('leap year')
        else:
            print('not leap')
    else:
        print('leap year')
else:
    print('not leap year.')


# In[ ]:




