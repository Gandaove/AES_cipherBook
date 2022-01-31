# AES_CipherBook

<font size = 6 color = 'red'>**Hi, GitHub!**</font> 

## Before start

I'm gandaove, new of GitHub. I have been registered my GitHub account for a few years now, always "learning" the code of masters. So yeah, that's my first project I upload to GitHub.

Once I just browsed the website, and I found a kind of "useful" tool named **1password**, that caught my interest. So I decided to do a similar thing. And... It's just came out!



## Modules to Import 

* **Crypto.Cipher(pycryptodome)**: It's the most important module, it provide the main algorithm of AES-256.
* **base64**: After the content is encrypted, base64 will package it for 2nd time.
* **os.system**: System module, mainly used to suspend.
* **time.sleep**: Time module, used to suspend.
* **hashlib**: Calculate **Key**'s hash. I'll mention it below.



## Compiler Environment

* Windows 10 64bit 20H2
* Python 3.9.5
* VSCode (pyinstaller for package)
* Use Windows 7 64bit(Python 3.8.10) to pack for compatibility and pure environment.



## Main Features

This is a software which could storage your accounts and passwords as a local file safely. Set a Key for your **cipherBook** and remember it, So you could add your complex message securely!



## Instruction

- **Key**: The key you set on cipherBook
- **Question**: Tip message
- Attention: You must input your file-path correctly whatever you want to do in 1st menu. I suggest you input the FULL-path of your file(E:/Cache/xxx.key) . You should know when you just input your file name, the program will find your file in current path.
- When you use this program for first-time, you should create a cipherBook. Please input **1** when you get into this program. And you could modify your book according to menu prompts.
- Attention: you must set your **Key, Question** to make sure you could use your cipherBook properly.(If you're not set, Key will be initialized as *'None'*) Make sure choose **y** when you quit program and you want to save your change.
- Now you have a cipherBook. If you want to check or modify, you should input your **Key** correctly.



## Main Logic

I plan to build a password manual  **cipherBook** which could save your passwords as local file safely. File could storage as plaintext, others cannot break it easily at same time. Only you know the important **Key**. 

After learning through website and my "careful selection", I adopted **AES-256** with CBC, padding by **PKCS7**. 

This require several parameters: *Key, IV, content* 

* **Key**: Due to the block encryption feature of CBC, it need length of 32 bytes string as key. Here, I encrypt each letter of your **Key** with **sha512** and connect, then use the concatenated string to convert to bytes format with **sha256**. In this way, could meet the requirement of **AES-256** with 32 bytes.

* **IV**: Similarly, IV need 16 bytes as padding. In order not to duplicate with **Key**, I made a small change: Take first half of **Key** with **sha512**, turn to bytes format with **md5** after connection. 16 bytes exactly.

* **Content**: Of course, that's the content you want to storage. Using dictionary storage.

	As new version, format could be more openness, allowed to nesting. But you still need to follow the basic rule of dictionary.

	```python
	dict = {'name':{'username': 'password'}}		# old version
	
	
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
	'''											# new version
	```

* About **PKCS7**

	**PKCS7** prescript a kind of padding standard to make sure **AES-256(CBC)** could encrypt and decrypt correctly. Usually, Key padding standard is 16 bytes, here I set it as double. Padding content are ASCII(1~31).

* About format of storage file

	In fact, there are no strict circumstance on file format. First line of file is tip sentence. Second line is **key** with double hash(hex). Third is content dictionary.

So, core idea is: first input your content, and turn the content dictionary to string, fill with padding function. Encrypt the key you typed with double hash(sha256) as **Key**. First half of **Key** treat as **IV** through double hash(md5). Using base64 for further packaging.

~~I think my opinion have some innovation.~~ 



## Main Module

- AES_cipherBook

	Main function part, mainly to call large modules.

- Function

	Mark functions more specifically, include create, read cipherBook and manipulate part.

- Modify_dict

	Modifying module

- Security

	Encrypt, verify module

- Menus

	Menu module

- Error_res

	Part of Error, quit solution module

- Input

	Input module(support ctrl+c to cancel input)



## Defects && Improvements

For definitely, even through I have some innovation opinions, the whole program still need to improve. Well, I have to admit that's a project of impulse. v1.0 took only 4 days.

1. Too reliance on Python modules. I could join more original functions.
2. ~~The structure of project is cumbersome, could be more optimization.~~
3. Currently only adaptation to Windows.
4. Potential Compatibility problem.
5. No GUI. Looks particularly monotonous with black console interface.
6. Multi-language support.
7. ~~Monotonous storage mode. Now only `name: {username: password}` is available.~~
8. I'm considering adding some rules of password detection. Your password's strength could be evaluated and give you suggestions.
9. Plaintext is easy to destroy. The file format could package further or encrypt.
10. Sync to xxxcloud.



## Update Logs

### v1.0

My first product version.



### v1.1

My first upload version. I improved program structure, fixed Chinese input problem and several bug. For compatibility reasons, I packaged .exe file on the pure environment of Windows 7 virtual machine.



### v1.2

A great update. This includes:

1. Rebuild code. All code is modularized by function to enhance readability.
2. Update algorithm of hash, make the break harder.
3. Delete set of **answer**. For now, **question** could used for tip.
4. Expanding format of storage. Expanded from storing only accounts & passwords to a more free format. Add new **level** hierarchy concept. You could expand  the storage tiers infinitely. Support storage on same tier.