# DiscussHub

DiscussHub is a Full Stack forum, which runs on Heroku.

Users can log in or log out, enter or create posts, comment, like/unlike posts, and delete the posts they created

The live version can be found on this link https://discusshub-f37fbed8aa3d.herokuapp.com/

<a href="https://ibb.co/kmfppZG"><img src="https://i.ibb.co/5KyddZ1/Am-IResponsive.png" alt="Am-IResponsive" border="0"></a>

## Features

- The User can log in or log out
- Users can register on the website

<a href="https://imgbb.com/"><img src="https://i.ibb.co/2v5NLgd/LogIn.png" alt="LogIn" border="0"></a>

<a href="https://ibb.co/znSgTdm"><img src="https://i.ibb.co/yf8Cc2N/Register.png" alt="Register" border="0"></a>

- The user will recive messages when they login/logout and when they post a comment

<a href="https://imgbb.com/"><img src="https://i.ibb.co/sWxv2FN/Messages-And-Filter-Search.png" alt="Messages-And-Filter-Search" border="0"></a>

- The user can also search topics based on a category

<a href="https://imgbb.com/"><img src="https://i.ibb.co/n8JLrzj/Search-Filter.png" alt="Search-Filter" border="0"></a>

- Users can create posts 

<a href="https://ibb.co/8PznmS7"><img src="https://i.ibb.co/3Sf5TLC/Create-Post.png" alt="Create-Post" border="0"></a>

- Users who created a Post can delete it if they want

<a href="https://ibb.co/GFtmHbk"><img src="https://i.ibb.co/N7mRTHp/Delete-Post.png" alt="Delete-Post" border="0"></a>

- Users can comment on a post or like/unlike the post if they are logged in

<a href="https://ibb.co/vVjHMN3"><img src="https://i.ibb.co/ZGMVbQB/Comment-Like.png" alt="Comment-Like" border="0"></a>

- The admin page is working properly and every function i've tested works

<a href="https://ibb.co/Xxdw5Tj"><img src="https://i.ibb.co/LdqGgfY/Admin-Page.png" alt="Admin-Page" border="0"></a>

## Testing

- Test : User loads the landing page <br>
    -- Result : Page display without error both logged in or out, all page content is displayed properly and the navigation bar is working as expected

- Test : User tries to log in or out <br>
    -- Result : The log in/out functions are working properly and the user is prompted to confirm if he want to log out.

- Test : Creating a Post <br>
    -- Result : After the user create a post he get redirected on the post detail page with a message for a succesul post creation.

- Test : Leaving a comment <br>
    -- Result : The logged in user can leave a comment receiving a message that his comment was posted successfuly and awaiting admin approval.

- Test : Deleting a post <br>
    -- Result : The user who created the post can delete it and the function works properly and receiving a confirmation for deleting the post, User being redirected back on the Home page without any issues.

- Test : Filter category <br>
    -- Result : The user can filter posts based on a category and the function works properly displaying only the posts that have been created with said category.

- Test : Admin page <br>
    -- Result : Admin page works properly and the admin can create, delete, approve comments, posts and categories on the admin panel.

- Test : Like/Unlike <br>
    -- Result : Like/Unlike function works as intended, Users who are logged in can like a post

- Test : Site pagination <br>
    -- Result : Site pagination works properly, when there are more than 6 posts created on the page the posts are shown on a different page.

- Test : Uploading a photo <br>
    -- Result : When creating a new phost the photo upload works properly and the photo is displayed 

- Test : Register user <br>
    -- Result : The register function works as you can register as a new user with password matching and complexity requirement 

## Bugs

- Edit/Delete Comment <br>
    -- I tried implementing the Edit/Delete function for users who wrote the comments but couldn't find a way to do it. As the only way i found would give me an error from the database saying the values can't be null and getting an error. Did not Implement in the end.



## Deployment

The project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
    - Clone this repository
    - Create a new Heroku app
    - Set the buildpacks to Python
    - Link the Heroku app to the repository
    - Click on Deploy

## Credits

- Code Institute for providing a base forum like website(I think therefore I blog) where I could improve and adapt based on what I needed to do.

   

