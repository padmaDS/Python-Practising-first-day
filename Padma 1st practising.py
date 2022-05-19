#!/usr/bin/env python
# coding: utf-8

# In[1]:


"padma" = 10


# In[2]:


a = 10


# In[3]:


a


# In[4]:


a+2


# In[5]:


a-2


# In[6]:


a/2


# In[7]:


a*2


# In[8]:


type(a)


# In[9]:


b = 10.5


# In[10]:


b


# In[11]:


type(b)


# In[12]:


b+5


# In[13]:


b-5


# In[14]:


b*5


# In[15]:


b/5


# In[16]:


b.real()


# In[17]:


b.real[]


# In[18]:


a.conjugate()


# In[19]:


b.conjugate()


# In[20]:


b.as_integer_ratio()


# In[21]:


b.fromhex()


# In[22]:


b.hex()


# In[23]:


b.imag()


# In[24]:


a.imag()


# In[25]:


c = "padma"


# In[26]:


c


# In[27]:


type(c)


# In[28]:


c.imag()


# In[29]:


c+1


# In[30]:


c+'1'


# In[31]:


c+"12345"


# In[32]:


d= "True"


# In[33]:


d


# In[34]:


d = True


# In[35]:


d


# In[36]:


True


# In[38]:


type(d)


# In[39]:


d.as_integer_ratio()


# In[40]:


d.bit_length()


# In[41]:


d.conjugate()


# In[42]:


d.denominator()


# In[45]:


d."denominator()"


# In[46]:


True + False


# In[47]:


True-False


# In[48]:


True+True


# In[49]:


False*False


# In[50]:


True/False


# In[51]:


False/True


# In[52]:


e = [123, "abc", 2, 5,]


# In[53]:


e


# In[54]:


type(e)


# In[55]:


e.real()


# In[56]:


e.append()


# In[57]:


e.copy()


# In[58]:


e


# In[60]:


e.count("abc")


# In[61]:


e.count(2)


# In[62]:


e.


# In[63]:


e.clear(1)


# In[64]:


e.clear()


# In[65]:


e


# In[66]:


e = [12, 34, 56, 78, "abc" , "def"]


# In[67]:


e


# In[68]:


e.extend()


# In[69]:


e.extend(89)


# In[70]:


e.index()


# In[71]:


e.insert()


# In[72]:


e.insert(76)


# In[74]:


e.pop(2)


# In[75]:


e


# In[76]:


e.remove(12)


# In[77]:


e


# In[78]:


e.reverse()


# In[79]:


e


# In[80]:


e.sort()


# In[81]:


e.sort("e")


# In[82]:


f = {123, "abc", 456, "bnm", 5.4, 123.56, "padma"}


# In[83]:


f


# In[84]:


type(f)


# In[85]:


f.add("bujji")


# In[86]:


f


# In[87]:


f.copy()


# In[88]:


f


# In[89]:


f.difference()


# In[90]:


f.difference_update()


# In[91]:


f


# In[93]:


f.discard()


# In[94]:


f


# In[95]:


f.intersection()


# In[96]:


f.intersection_update()


# In[97]:


f


# In[98]:


f.isdisjoint()


# In[100]:


f.issubset(1)


# In[101]:


f.issuperset()


# In[102]:


f.pop()


# In[103]:


f


# In[104]:


f.remove(123)


# In[105]:


f


# In[106]:


f.symmetric_difference()


# In[107]:


f.symmetric_difference_update(123)


# In[108]:


f.union()


# In[109]:


f.update()


# In[110]:


f


# In[115]:


g = {12 : 34 , 34 : 56 , 78 : 98, "padma" : "bujji"}


# In[116]:


g


# In[117]:


type(g)


# In[118]:


h = ("tyru", "bec" , 123, 10.5, 50.6)


# In[119]:


h


# In[120]:


type(h)


# In[121]:


e


# In[122]:


type(e)


# In[123]:


type(f)


# In[124]:


type(g)


# In[125]:


type(h)


# In[126]:


g.values()


# In[127]:


g


# In[129]:


g.fromkeys(1)


# In[130]:


g.items()


# In[131]:


g.keys()


# In[132]:


g.setdefault(3:5)


# In[134]:


g.setdefault(12)


# In[135]:


g.setdefault("padma")


# In[136]:


h


# In[137]:


h.count(123)


# In[138]:


h.index()


# In[139]:


h.index("bec")


# In[140]:


h.index(50.6)


# In[141]:


f


# In[142]:


type(f)


# In[143]:


d


# In[144]:


d.as_integer_ratio()


# In[145]:


e


# In[146]:


e.index(34)


# In[147]:


f


# In[148]:


type(f)


# In[149]:


s = "padmavathi"


# In[150]:


s


# In[151]:


type(s)


# In[152]:


s.capitalize()


# In[153]:


s.casefold()


# In[156]:


s.center(3)


# In[157]:


s.center(10)


# In[158]:


s.center(1000)


# In[159]:


s.count('a')


# In[160]:


s.count('p')


# In[161]:


s.encode('t')


# In[162]:


s.endswith('r')


# In[163]:


s.endswith('i')


# In[164]:


s.startswith('b')


# In[165]:


s.startswith('p')


# In[167]:


s.expandtabs()


# In[169]:


s.expandtabs(3)


# In[171]:


s.expandtabs(1000)


# In[176]:


s.expandtabs('*')


# In[177]:


s.find('t')


# In[178]:


s.find('i')


# In[179]:


s.format()


# In[181]:


s.format("i")


# In[182]:


s.format('p')


# In[183]:


s.format({'p' and 'i'})


# In[184]:


s.format({'a' and 't'})


# In[185]:


s.format_map('h')


# In[186]:


s.format({'padma' and 'vathi'})


# In[187]:


s.format_map({'padma' and 'vathi' })


# In[188]:


s = "padmavathi ayyan athia and bujji"


# In[189]:


s


# In[190]:


s.index('k')


# In[192]:


s.index('i')


# In[193]:


s.index('y')


# In[194]:


s.isalnum()


# In[195]:


s.isalpha()


# In[196]:


s = "padma123 this is my first class of practising python"


# In[197]:


s


# In[199]:


s.isalnum()


# In[200]:


s = 'padma123'


# In[201]:


s


# In[203]:


s.isalnum()


# In[205]:


s.isalpha()


# In[206]:


s.isascii()


# In[207]:


s.isdecimal()


# In[208]:


s.isdigit()


# In[209]:


s = 1234567543


# In[210]:


s


# In[211]:


s.isdigit()


# In[212]:


s = 'padma123'


# In[213]:


s


# In[214]:


s.isidentifier()


# In[215]:


s.islower()


# In[216]:


s.isnumeric()


# In[217]:


s.isprintable()


# In[221]:


s.isspaces()


# In[222]:


s.istitle()


# In[223]:


s.isupper()


# In[226]:


s.join("i")


# In[227]:


s.join('')


# In[228]:


s


# In[229]:


" ".join('padma')


# In[230]:


"b".join('papa')


# In[231]:


"  ".join('athika')


# In[233]:


'abc'.join('god')


# In[234]:


"god".join('pandu')


# In[235]:


s


# In[236]:


s.center(20,'*')


# In[245]:


s.center(50, '@')


# In[246]:


s.center(100,'%')


# In[249]:


s = "ineuron"


# In[248]:


s


# In[250]:


s


# In[251]:


s[1:6]


# In[252]:


s[1:3]


# In[253]:


s = "this is my first class of python practising"


# In[255]:


s


# In[256]:


s[1:10:2]


# In[257]:


s[3:20:2]


# In[258]:


s[0:10]


# In[260]:


s[-1:-10]


# In[261]:


s[10:15]


# In[263]:


s[-10:-17:-2]


# In[264]:


s


# In[265]:


s[0:50:5]


# In[266]:


s[-20:-1:3]


# In[267]:


s[:5]


# In[268]:


s[::]


# In[269]:


s[2:]


# In[270]:


s[::2]


# In[271]:


s


# In[272]:


s[::-1]


# In[274]:


s.join("reverse")


# In[275]:


s[-1:-1]


# In[276]:


s+'3'


# In[277]:


s+'3456'


# In[278]:


s+str(45678)


# In[279]:


len(s)


# In[280]:


s = "pandupapa"


# In[281]:


s


# In[282]:


s*2


# In[ ]:




