# LibraryProject
--This was an experimental project, the second time I have ever coded.-- April 2020

In April 2020, Springer made around 400 books about various subjects free to download. Obviously I wanted to download them all, I didn't even think when I would be able to read them. Then I realized that I needed to do a minimum of 3 clicks in order to get a file without extension and even without the name of the book. Instead of doing the manual work, I thought of writing a program which could visit the book link and pull the book file from the website. It even read the excel file for the names of the books and saved the downloaded files with their corresponding names and extension (pdf).

After 15 hours of dealing with errors and learning new Python libraries, one click was all I needed. Upon running the program, I felt like a hacker, as a "computer stimulated chrome" window popped up on my screen and started to go through the links one by one. However, an unexpected error occured when my program couldn't find the download icon for one of the books in the order. Shortly after, I understood that this wasn't a lone case among the published links and there were more than one page without a download option.

Here, I could have manualy exclude the links by spliting the process as many times according to the number of the books I couldn't download, giving the program a different interval to go through each time. But again, my goal was to squeeze all of that work into one click. So, I told my program to pass on the links with a price tag, since it seemed as a reasonable exclusion criteria. Yet, when I run the program, it failed again. Even when it managed to break through the first obstacle, it failed to recognize the price tag on another page.

I tried to solve this problem by adding some other keywords to pass on, such as "Buy". Once again it excluded some of the pages with the word "Buy", but left some of them behind for a reason I couldn't understand. After working on this issue one more day, I felt like I needed to change the backbone of my code and maybe write a new one, since I wasn't able to grasp the reason behind the error. Maybe, my HTML knowledge was lacking.

The program was never completed, becuase I was exhausted from two days of constant work on it. When I was back on work, none of the books were free to download anymore. Despite the fact that my program didn't work, I am still very happy about what I could accomplish after two days of binge-learning, experimenting and coding. Today, this project prooves to me that I can, and I will code in my life.

Thank you for reading :)
