# <!-- BLOG-POST-LIST:START  -->Project : Medical Image Processing Applications<!-- BLOG-POST-LIST:END  --> 

## **Introduction** 

This project contains development of an application to evaluate a Medical Image and provide a parameter which will help the doctors in evaluation of the disease.

An Image of a specific body part (Back for project) of a patient having Fungal or Bacterial Infection is provided to the application and this application will calculate the Percentage(Relative Area) of the infected region with respect to the body part having infection.

This applicaion also provides an images of the Infected Area separated from the body.

## **Implementation Steps** 

Step 1 : **Select a language for Implementation** - Python is used in this project for developing as it has [Scikit-Learn](https://scikit-learn.org/stable/) Library which has many tools that can be used for Image Processing.

Step 2 : **Select an optimal Algorithm** - [Entropy](https://scikit-image.org/docs/dev/auto_examples/filters/plot_entropy.html) from Scikit-Image is used.

Step 3 : **Tuning of Parameters** - There are many attributes in the implementation which needs tuning to improvise accuracy.

Step 4: **Create an User Interface** - [Kivy](https://kivy.org/#home) is used. 

Step 5: **Testing** -  Different images are used for testing 

## **Implementation** 
The Python code can be seen here - [main.py](main.py) and Kivy code here - [IP.kv](IP.kv) 
This is the image used for creating the algorithm.

<p align="center">
  <img src="https://github.com/B19EE075/Design-Project/blob/6ab09269da55fa3669f0759cc4a2b52e91a866e2/Assets/back.jpg" width="200" title="hover text">
  
</p>

A test run of the application is shown.
This is the homepage of the app.

<p align="center">
  <img src="https://github.com/B19EE075/Design-Project/blob/f3b0809153f92181a6eb2571e8188bcded7076ba/Assets/1.png" width="200" title="hover text">

An image is selected by clicking the select button on the homepage. It is shown in minimized form.
  
<p align="center">
  <img src="https://github.com/B19EE075/Design-Project/blob/86e7332b571733679d8e8bf4d0a7c6d4f5617e27/Assets/3.png" width="200" title="hover text">

Then the submit button will start the processing and will show the result in 10 secs (average).
The Infected area for the above selected image can be seen below i.e. Infected area = 7.662
<p align="center">
  <img src="https://github.com/B19EE075/Design-Project/blob/86e7332b571733679d8e8bf4d0a7c6d4f5617e27/Assets/4.png" width="200" title="hover text">

The infected part is shown separately with the real image.
<p align="center">
  <img src="https://github.com/B19EE075/Design-Project/blob/86e7332b571733679d8e8bf4d0a7c6d4f5617e27/Assets/5.png" width="200" title="hover text">
  
## **Conclusion**  
So the application is showing the results and can be used to check the progress of the treatment by evaluating the area of the infection.
 
The application is still under development and improvisation and can be used by anyone having knowledge of python and kivy using the source code 
 
The apk file will also be available here which can be used by anyone easily.
  
  
  
  
  
  
  

