# Project work load

## Authentication System `[ayman]`

[Deadline]: # Date: 2022-05-05

### Registration ❤️👌 ✅

- First name
- Last name
- Email
- Password
- Confirm password
- Mobile phone [validated against Egyptian phone numbers] ❤️👌 ✅
- Profile Picture

### Activation Email after registration ❤️👌 ✅

- Once the user registers he should receive an email with the
activation link. The user shouldn’t be able to login without
activation. The activation link should expire after 24 hours. 

`todo` : We just need to make the user isActive = false by default until he click on the activation mail

### Login

- The user should be able to login after activation using his email
and password. ❤️👌 ✅
- `Bonus`: Allow users to login with facebook account

### Forgot Password (Bonus)

- The user should have an option to reset his password if he
forgot it to receive a password reset link to his email

## User Profile, The user can view his profile which [`ashraf`]

- He can view his profile
- He can view his projects
- He can view his donations
- He can edit all his data except for the email
- He can have extra optional info other than the info he added
while registration (Birthdate, facebook profile, country)
- User can delete his account (Note that there must be a
confirmation message before deleting)
- `Bonus`: User must enter his password to delete his account

## Projects: `[amr]`

- The user can create a project fund raise campaign which contains:
- Title
- Details
- Category (from list of categories added previously by admins)
- Multiple pictures
- Total target (i.e 250000 EGP)
- Multiple Tags
- Set start/end time for the campaign

### project ui

- Users can view any project and donate to the total target
- Users can add comments on the projects
- Bonus: Comments can have replies
- Users can report inappropriate projects
- Users can report inappropriate comments
- Users can rate the projects
- Project creator can cancel the project if the donations are less than
25% of the target
- Project page should show the overall average rating of the project
- Project page should show the project pictures in a slider
- Project page should show 4 other similar projects based on project
tags

### Homepage should contains the following [`hafez`]

- A slider to show the highest five rated running projects to encourage
users to donate
- List of the latest 5 projects
- List of latest 5 featured projects (which are selected by the admin)
- A list of the categories. User can open each category to view its
projects
- Search bar that enables users to search projects by title or tag
Similar Projects to get some inspiration :)
https://www.gofundme.com https://www.kickstarter.com https://www.crowdfunding.com
Note: Starting to work on bonus points without completing the essential
features makes no sense

## Deployment

> deployment with doker compose `[ayman]`

1- doker contianer for:

- postgres databsae

- react container

- django container
