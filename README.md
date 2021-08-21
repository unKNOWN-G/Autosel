# <a style="text-decoration: none" id="title" >Autosel</a>
Autosel is a Python package that automates sending emails, Whatsapp text, images, videos, and audio messages along with other functionalities like creating a group and spam bot.

**Libraries Used**: Selenium, gTTS 
\
&nbsp;
***
## <a style="text-decoration: none" id="features" style="color:gren;">Main Features</a>
1) <div ><b>&nbsp;&nbsp;Bolding</b> Functionality in Emails</div>
   
   * Specific Parts of an Email can now be bolded using `autosel`.
2) <div ><b>&nbsp;&nbsp;Spam Bot</b> in Whatsapp</div>

    * Using `autosel`, we can send a message multiple times (spam) to a user(s).
3)  <div > <b>&nbsp;&nbsp;Audio Sender</b> in Whatsapp</div>  

    * Text messages can now be sent as voice clip using `autosel`
4) <div ><b>&nbsp;&nbsp;automate sending all types of media in Whatsapp</b> in Whatsapp</div>

    * Using `autosel`, we can automate sending Text, Images, Videos, Documents, and Audio Clips.
5) <div ><b>&nbsp;&nbsp;Group Creator</b>  in Whatsapp</div> 
 
    * Process of creating a group and adding participants, and sending invites is automated by `autosel`


&nbsp;
***
## <a style="text-decoration: none" id="contents" >Table of Contents</a>
- [Package-name](#title)
- [Main Features](#features)
- [Table of Contents](#contents)
- [Prerequisites](#pre)
- [Installation](#install)
- [What Classes are present in this Library?](#what)
- [Email Class](#email)
    - [Description](#email-desc)
    - [What Methods Do we have?](#email-what)
    - [Importing and assigning Email class](#email-import)
    - [Methods](#email-method)
- [Whatsapp Class](#whatsapp)
    - [Description](#whatsapp-desc)
    - [What Methods Do we have?](#whatsapp-what)
    - [Importing and assigning Email class](#whatsapp-import)
    - [Methods](#whatsapp-method)

***
## <a style="text-decoration: none" id="pre" >Prerequisites</a>
- Chrome Driver  
   Download the suitable version of your chrome driver from [**here**](https://chromedriver.chromium.org/downloads) which is similar to the version of your chrome browser. The Chrome version can be found in `Settings/About Chrome`

- Selenium
    ```
     pip install selenium
     ```
- gTTs
    ```
    pip install gtts
    ```
***
## <a style="text-decoration: none" id="install" >Installation</a>
- Using PIP
    ```
    pip install autosel 
    ```
- Using Conda
    ```
    conda install autosel
    ```



***
## <a style="text-decoration: none" id="what">What Classes are present in this Library?</a>
- [Email](#email)
- [Whatsapp](#whatsapp)
## <a style="text-decoration: none" id="email" >Email Class</a>

### <a style="text-decoration: none" id="email-desc" >A.  Description  </a>

This Class automates the process of sending E-mails to multiple recipients. 
Using the sender_mail and sender_password credentials as input along with mail_subject and mail_body as input, Mails can be sent to **Multiple recipients individually**.

There's an additional functionality of Bolding the content in the body. This feature can be used by alternatively giving the texts in the mail_body list with normal and bold texts [ "Normal text1", "Bold Text 1", "Normal text 2", "Bold Text 2" ....]
>**Note:**
>- To input Multiple lines of string, use triple quotes.                                             
>- It is advised to use organization-specific sender_email that (or) gmails that arent created on this device to avoid security issues with google verification.  


### <a style="text-decoration: none" id="email-what">B. What Methods do we Offer?</a>
- Email Class
    - [send_mails](#mails)

### <a style="text-decoration: none" id="email-import">C. Importing and assigning Email class</a>
- Importing the `Email` Class  
    
    ```
    from autosel import Email
    ```
- Assign `Email` Class to a Class Variable:
    \
    The Email Sender Class takes inputs as `sender_email`, `sender_password`, `mail_subject`, `mail_body`

    >The Bolding Functionality can be use in body of the Email by alternatingly giving the texts in `mail_body` variable as shown below.  
    >[ "Normal text1", "Bold Text 1", "Normal text 2", "Bold Text 2" ....]

    *Input Parameters*:

    >`sender_email`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: str, Mail ID of the sender
    \
    >`sender_password`&nbsp;: str, Password of the sender
    \
    >`mail_subject`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: str, Subject of the Email 
    \
    >`mail_body`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: list, List of stings alternatively given with Normal and bolding texts.
    ```
    var = Email(sender_email: "abc@gmail.com", sender_password: "12345678", mail_subject: "Hello World!", mail_body: ["""This is a Normal Text, ""","""This is a Bolded Text"""])
    ```
### <a style="text-decoration: none" id="email-method">D. Methods  </a>
- #### <a style="text-decoration: none" id="mails">send_mails</a>

    This method automatematically sends emails to the recipients.   
    Mails can be sent to ***Multiple recipients*** individually by adding their names in the `emails` list.

    *Input Parameters:*  

    >`driver_path`: str, Chrome Driver Address.
    \
    >`emails`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: list, List of Emails to which emails are to be sent.  

    ```
    var.send_mails(driver_path: "", emails: ["",""]) 
    ```  
    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130320925-9ace9aea-59e7-48a5-b410-ff21e826101b.mp4)  


******

## <a style="text-decoration: none" id="whatsapp" >Whatsapp Class</a>
### <a style="text-decoration: none" id="whatsapp-desc">A. Description</a>


### <a style="text-decoration: none" id="whatsapp-what">B. What Methods Do we have?</a>
- Whatsapp Class
    - [spam_bot](#spam)
        \
    &nbsp;
    - [send_text](#text)
    - [send_image](#image)
    - [send_document](#document)
    - [send_audio](#audio)
    - [create_group](#groupmaker)
        \
    &nbsp;
    - [close_whatsapp](#closer)
\
&nbsp;
### <a style="text-decoration: none" id="whatsapp-import">C. Importing and assigning Email class</a>
- Importing the Whatsapp Class
    ```
    from autosel import Whatsapp
    ``` 
- Assign `Whatsapp` Class to a variable

    To initialize the the chrome driver and to login got whatsapp. The usage_data_directory is used to store the QR code information to avoid multiple scanning.   

    *Input Parameters :*  

    >`driver_address` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : str, Address of Chrome Driver.  
    >`usage_data_directory` : str, Stores data to help logging multiple times seamless by passing QR code.

    *Code*:
    ```
    var = Whatsapp(driver_address:"", usage_data_directory: "")
    ```

### <a style="text-decoration: none" id="whatsapp-method">D. Methods</a>
- #### <a style="text-decoration: none" id="spam">spam_bot</a>
    - This method is used to send repeated texts (Spam) to the same person.
    - Messages can be sent to ***Multiple recipients*** also by the contact names in `name` list.  

    *Input Parameteres :*  
    > `name` &nbsp;: list, Names of the person to whom these messages are to be sent.     
    > `msg` &nbsp;&nbsp;&nbsp;: str, Message.  
    >`count` : int, Number of Messages.

    *Code :*

    ```
    var.spam_bot(name: ["",""], msg: "", count:)
    ```
    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130320935-bdbbe52d-a247-4679-aee5-ad728449a22d.mp4) 

---
- #### <a style="text-decoration: none" id="text">send_text</a>
    - This method is used to automatically send messages to the recipient.  
    - ***Multiple messages*** can be sent by adding messages into the `msg` list.  
    - The same set of images, videos can be even sent to ***Multiple people*** by adding names into the `name` list.  

    *Input Parameteres :*   
    >`name`&nbsp;&nbsp;&nbsp;&nbsp;: list, List of all contacts to which it should be send in string format.  
    >`msg` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: str, Message to be sent.   
    >`select` : bool, Confirm if a particular command should be there on not. It has a Default Value true  

    *Code :* 
    ```
    var.send_text(name: ["",""], msg: "")
    ```
    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130320945-40fbd00c-a3f7-48f3-a65b-275f8c270b3d.mp4) 

---
- #### <a style="text-decoration: none" id="image">send_image</a>  
    - This method is used to automatically send image or video to the recipient. 
    - ***Multiple Images, Videos*** can be sent by adding the file address with extension in the `file_address` list. 
    - The same set of images, videos can be even sent to ***Multiple people*** by adding names into the `name` list.  
    - Accepts all formats of image and videos.  

    *Input Parameteres :*   
    >`name`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: list, List of all contacts to which it should be send in string format.  
    >`files_address`&nbsp;: list, Contains strings of address of files to be sent stored in list.   
   >`select` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: bool, Confirm if a particular command should be there on not. It has a Default Value true  

    *Code :*
    ```
    var.send_image(name: ["", ""], files_address: ["",""], select: bool = True)
    ```
    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130320952-2cf044a9-6f57-46f9-abfc-c2aa754aa865.mp4) 

---            
- #### <a style="text-decoration: none" id="document">send_document</a>  
    - This method is used to automatically send files as documents to the recipient.
    - ***Multiple Documents*** can also be sent to the recipient by adding the files address in `file_address` list.
    - This same set of documents can be even sent to ***Multiple people*** by adding names into the `name` list.
    - Accepts all formats. 

    *Input Parameteres :*   
    >`name`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: list, List of all contacts to which document should be sent.  
    >`files_address`&nbsp;: list, Contains strings of address of files to be sent stored in list.   
    >`select` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: bool, Confirm if a particular command should be there on not. It has a Default Value of true  

    *Code :*
    ```
    var.send_image(name: ["", ""], files_address: ["",""], select: bool = True)
    ```
    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130320955-6752b1fc-7cc7-4c30-856b-eea564a63cf3.mp4) 
 
- #### <a style="text-decoration: none" id="audio">send_audio </a> 
    - This method converts the given message into a audio recording and will send to the recipient.
    - The audio file can be sent to multiple recipients by adding recipients into `name` list.  

    *Input Parameters:*  
    >`name`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: list, List of all contacts to which it should be send in string format.  
    >`msg`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: str, Stores the message in string format.  
   >`file_name`&nbsp;: list, Name of the Audio File.  
    >`file_dir`&nbsp;&nbsp;&nbsp;: str, name of file directory.   
    >`select`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: bool, Confirm if a particular command should be there on not. It has a Default Value of true    


    *Code :*
    ```
    var.send_audio(name: ["", ""], files_address: ["",""])
    ```     

    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130320960-4f9ed498-6cb6-47ba-8ed6-abe15481d020.mp4)
---    
- #### <a style="text-decoration: none" id="groupmaker">create_group </a>
    - This method is used to create a whatsapp group.
    - Using the contact names given in `group_list` and group name in `group_name` the whatsapp group is made. 
     
    *Input Parameters:*  
    >`group_list` : list, Stores the list of names(str) to be added in group in a list.  
    >`group_name` : str, Name of the group.  
    >`text_dir`&nbsp;&nbsp;&nbsp;&nbsp;: str, This is an alternate way of giving the list of group members and the group name by storing in a .txt file. Each line in the text file denoteds one contact name and teh name at the end of text file denote Group name. Default filename is take as `group_name.txt` in the project directory



    *Code :*
    ```
    var.create_group(group_list: ["",""], group_name: "")
    ```  
    *Demo :* To watch a quick demo, Click [here](https://user-images.githubusercontent.com/60328300/130328623-7141b762-641e-4cb7-986b-db40017aea78.mp4) 

---
- #### <a style="text-decoration: none" id="closer">close_whatsapp</a>  
    - This method is used to close the running chrome driver.

    *Input Parameters:*  None

    *Code :*
    ```
    var.close_whatsapp()
    ```
***
## License
### [**MIT**]()

## Contact
[<img src="https://user-images.githubusercontent.com/60328300/130331837-420bf373-2f57-4752-9074-81830f7059ec.png" width="10%" height="7%">](https://github.com/unKNOWN-G/autosel)

### Made with <3 from unKNOWN-G</div>
