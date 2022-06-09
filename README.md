# AES_CipherBook

<font size = 6 color = 'red'>**Hi, GitHub!**</font> 

## Before start

I'm Gandaove, new to GitHub. I have registered my GitHub account for a few years now, always "learning" the code of masters. So yeah, that's the first project I uploaded to GitHub.

Once I browsed the website, I found a kind of "useful" tool named **1password**. That caught my interest. So I decided to make a similar software. And... It just came out!



## Modules to Import 

- **Crypto.Cipher (pycryptodome)**: The most important module. It provides the main algorithm of AES-256.
- **base64**: After the content is encrypted, base64 will package it for a second time.
- **os.system**: System module, mainly used to suspend.
- **time.sleep**: Time module, used to suspend.
- **hashlib**: Calculate **Key**'s hash. I'll mention it below.



## Compiler Environment

- Windows 10 64bit 20H2
- Python 3.9.5
- VSCode (pyinstaller for packaging)
- Use Windows 7 64bit(Python 3.8.10) to pack for compatibility and a pure environment.



## Main Features

This is software that could store your accounts and passwords as a local file safely. Set a Key for your **cipherBook** and remember it, then you could add your complex message securely!



## Instruction

- **Key**: The key you set on **cipherBook**
- **Question**: The Tip message you set
- Attention1: You must input your file path correctly whatever you want to do in the 1st menu. I suggest you input the **FULL** path of your file(E:/Cache/xxx.key). When you just input your filename, the program will find your file in the current path.
- When you use this program for the first time, you should create a cipherBook. Please input **1** when you get into this program. And you could modify your cipherBook according to menu prompts.
- Attention2: you must set your **Key** and **Question** to make sure you could use your **cipherBook** properly (If you're not set, we will initialize Key as *'None'*). Make sure to choose **y** when you want to quit the program and save your change.
- Now you have a cipherBook. If you want to check or modify it, you should input your **Key** correctly.



## Main Logic

I plan to build a password manual **cipherBook** that could save your passwords as a local file safely. Others cannot break the file with ease. Only you know the important **Key**. 

After learning through the website and my "careful selection", I adopted **AES-256** with CBC, padding by **PKCS7**. 

This requires several parameters: *Key, IV, content*  

* **Key**: Due to the block encryption feature of CBC, it needs the length of 32 bytes string as the key. Here, I encrypt each letter of your **Key** with **sha512** and connect, then use the concatenated string to convert to bytes format with **sha256**. In this way, could meet the requirement of **AES-256** with 32 bytes.

* **IV**: Similarly, IV needs 16 bytes as padding. In order not to duplicate with **Key**, I made a small change: Take the first half of **Key** with **sha512**, turn to bytes format with **md5** after connection. 16 bytes exactly.

* **Content**: Of course, that's the content you want to store. Using dictionary storage.

	In the new version, the format could become more diverse (allowing nesting). But you still need to follow the basic rule of **dict**.

	```python
	# old version
	dict = {'name':{'username': 'password'}}
	
	# new version
	'''									# level concept
	twitter:							# level1
		account name: 111				# level2
		password:
			No.1: 000000				# level3
			No.2: 654321
		mention: Important!
	Gmail:								# level1
		account_name: 1111@gmail.com
		password: xxxx
	'''
	```

* About **PKCS7**

	**PKCS7** prescript a kind of padding standard to make sure **AES-256(CBC)** could encrypt and decrypt correctly. Usually, the Key padding standard is 16 bytes, here I set it as double. Padding content is ASCII(1~31).

* About format of storage file

	There is no strict requirement for the file format. The first line of the file is the tip sentence. The second line is **key** with a double-hash(hex). The third is the content dictionary.

So, the core idea is: first input your content, and turn the content dictionary to string, fill it with the padding function. Encrypt the key you typed with double-hash(sha256) as **Key**. The first half of **Key** is treated as **IV** through double-hash(md5). Using base64 for further packaging.

~~I think my opinion has some innovation.~~ 



## Main Modules

### AES_cipherBook

Main function part. Calling large modules mainly.

### Function

Mark functions more specifically, include creating, reading cipherBook, and manipulating parts.

### Modify_dict

Modifying module

### Security

Encrypting, and verifying module

### Menus

Menu module

### Error_res

Part of the Error and quit solution module

### Input

Input module(support ctrl+c to cancel input)



## Defects && Improvements

Even though I have some innovative opinions, the whole program still needs to be optimized. Well, I have to admit that's a project of impulse. After all, v1.0 took only 4 days.

1. Relying too much on Python modules. I could join more original functions.
2. ~~The structure of the project is cumbersome. Should be further optimized.~~
3. Currently, only adaptation to Windows.
4. Potential Compatibility problem.
5. No GUI. Looks particularly monotonous with the black console interface.
6. Multi-language support.
7. ~~Monotonous storage mode. Now only **name: {username: password}** is available.~~
8. I'm considering adding some rules for password detection. Your password's strength could be evaluated and give you suggestions.
9. Sync to xxxcloud.



## Update Logs

### v1.0

My first product version.  



### v1.1

My first upload version. I improved the program structure, fixed the Chinese input problem, and several bugs. For compatibility reasons, I packaged the .exe file on the pure environment of Windows 7 virtual machine.  



### v1.2

A great update. It includes:

1. Rebuild code. All code is modularized by function to enhance readability.

2. Update the algorithm of hash, it makes cracking become harder.

3. Delete **answer**. For now, the **question** could be used as a tip.

4. Expanding format of storage. 

	Expanded from `{account: password}` to a more optimized format. Add a new concept **level**. You could expand the storage tiers **infinitely** (for theoretically). Support storage on the same tier.