# VolunteerPhilippines


## Project Overview

The VolunteerPhilippines project is intended to provide useful information to anyone interested in doing volunteer work in the Philippines.

## Data Functionality

-Home page that displays volunteer organizations with brief overview of each

-User registration page/login/logout

-Return on investment page. Allows user to enter a dollar amount and displays the projected return for world development goals. Contains Copenhagen Consensus research information

-News page that displays stories related to volunteer work in the Philippines

## Data Model

-NewsPost

    -title (CharField)
    
    -content (TextField)
    
    -date_posted (DateTimeField)
    
    -related_image (Charfield)

-Organization

    -title (CharField)
    
    -information (TextField)
    
    -url (UrlField)
    
    -related_image (Imagefield)

-ReturnOnInvestment

    -project (CharField)
    
    -multiplier (IntegerField)
    
    -info (Charfield)


## Schedule

-Week 1

  - Start django project
  
  - Create Models
  
  - Create Homepage View
  
  - Create Blog View
  
-Week 2 
 
   - Create registration page view
    
   - Make templates with template inheritance 
    
   - Add organizations to homepage
    
   - Add blogposts/related news stories to blog section
    
-Week 3 

  - Create ROI page and view  
  
  - Make about pages for each organization listed
    
  - css/bootstrap styling
    






