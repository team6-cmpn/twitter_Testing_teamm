from element import BasePageElement
from locator import MainPageLocators
from locator import SignUpWithGooglePageLocators
from locator import SignUpPhoneOrMailPageLocators
from locator import SignInPageLocators 
from locator import MainPage2Locators
from locator import HomePageLocators
from locator import ExplorePageLocators 
from locator import NotificationsPageLocators
from locator import ProfilePageLocators
from locator import EditProfilePageLocators
from locator import AdminPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


#class TypeGoogleEmail(BasePageElement):
    #locator = "identifier"


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def click_SignUpWithGoogle_Button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SignUpGoogle)
        element.click()

    def click_SignUpWithPhoneOrMail(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SignUpPhoneOrMail)
        element.click()

    def click_SignIn(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SignIn)
        element.click()


class EnterGoogleEmailPage(BasePage):

    def click_EnterEmail(self, str):

        element = self.driver.find_element(*SignUpWithGooglePageLocators.EnterEmail)
        element.send_keys(str)

    def click_Next(self):
        element= self.driver.find_element(*SignUpWithGooglePageLocators.NextButton) 
        element.click()   



class SignUpPhoneOrMailPage(BasePage):

    def enter_Name(self, str):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Name)
        element.send_keys(str)
    
    def enter_Username(self, str):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Username)
        element.send_keys(str)

    def enter_Email(self, str):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Email)
        element.send_keys(str)

    def enter_Password(self, str):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Password)
        element.send_keys(str)

    def enter_Date(self, str):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Date)
        element.send_keys(str)
    
    def click_Next_1(self):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Next1)
        element.click()

    def click_Next_2(self):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Next2)
        element.click()

    def SignUpButton(self):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.SignUp)
        element.click()

    def click_Next_3(self):
        element = self.driver.find_element(*SignUpPhoneOrMailPageLocators.Next3)
        element.click()


class SignInPage(BasePage):
    def enter_EmailOrUsername(self, str):
        element = self.driver.find_element(*SignInPageLocators.EmailOrUsername)
        element.send_keys(str)

    def click_Next(self):
        element = self.driver.find_element(*SignInPageLocators.Next)
        element.click()

    def click_ForgetPassword(self):
        element = self.driver.find_element(*SignInPageLocators.ForgetPassword)
        element.click()

    def click_SignUp(self):
        element = self.driver.find_element(*SignInPageLocators.SignUp)
        element.click()
    
    def click_SignInGoogle(self):
        element = self.driver.find_element(*SignInPageLocators.SignInGoogle)
        element.click()
    
    def enter_Password(self, str):
        element = self.driver.find_element(*SignInPageLocators.Password)
        element.send_keys(str)

    def click_ForgetPassword_2(self):
        element = self.driver.find_element(*SignInPageLocators.ForgetPassword_2)
        self.driver.implicitly_wait(100)
        element.click()

    def click_LogIn(self):
        element = self.driver.find_element(*SignInPageLocators.LogIn)
        element.click()

    def enter_Username2(self,str):
        element = self.driver.find_element(*SignInPageLocators.FindYourTwitterAccount_Username)
        element.send_keys(str)

    def enter_Email2(self,str):
        element = self.driver.find_element(*SignInPageLocators.FindYourTwitterAccount_Email)
        element.send_keys(str)

    def click_Search(self):
        element = self.driver.find_element(*SignInPageLocators.Search)
        element.click()

    def click_next_2(self):
        element = self.driver.find_element(*SignInPageLocators.Next_2)
        element.click()


class MainPage2(BasePage):
    def click_Home(self):
        element = self.driver.find_element(*MainPage2Locators.Home)
        element.click()
    
    def click_Explore(self):
        element = self.driver.find_element(*MainPage2Locators.Explore)
        element.click()

    def click_Notifications(self):
        element = self.driver.find_element(*MainPage2Locators.Notifications)
        element.click()

    def click_Bookmarks(self):
        element = self.driver.find_element(*MainPage2Locators.Bookmarks)
        element.click()

    def click_Profile(self):
        element = self.driver.find_element(*MainPage2Locators.Profile)
        element.click()

    def click_Settings(self):
        element = self.driver.find_element(*MainPage2Locators.Settings)
        element.click()

    '''def click_Tweet(self):
        element = self.driver.find_element(*MainPageLocators.Tweet)
        element.click()'''

    def click_Username(self):
        element = self.driver.find_element(*MainPageLocators.Username)
        element.click()

    def click_Admin(self):
        element = self.driver.find_element(*MainPageLocators.Admin)
        element.click()

class HomePage(BasePage):
    def enter_Tweet(self, str):
        element = self.driver.find_element(*HomePageLocators.TweetBar)
        element.send_keys(str)

    def click_Tweet(self):
        element = self.driver.find_element(*HomePageLocators.TweetButton)
        element.click()

class ExplorePage(BasePage):
    def enter_Search(self, str):
        element = self.driver.find_element(*ExplorePageLocators.SearchBar)
        element.send_keys(str)
    
    def click_SearchButton(self):
        element = self.driver.find_element(*ExplorePageLocators.SearchButton)
        element.click()

class NotificationsPage(BasePage):
    def click_All(self):
        element = self.driver.find_element(*NotificationsPageLocators.AllButton)
        element.click()

    def click_Mentions(self):
        element = self.driver.find_element(*NotificationsPageLocators.MentionButton)
        element.click()

class ProfilePage(BasePage):
    def click_EditProfile(self):
        element = self.driver.find_element(*ProfilePageLocators.EditProfile)
        element.click()
    
    def click_Followers(self):
        element = self.driver.find_element(*ProfilePageLocators.Followers)
        element.click()

    def click_Following(self):
        element = self.driver.find_element(*ProfilePageLocators.Following)
        element.click()

    def click_FollowersFollowing(self):
        element = self.driver.find_element(*ProfilePageLocators.FollowersFollowing)
        element.click()

    def click_Tweets(self):
        element = self.driver.find_element(*ProfilePageLocators.Tweets)
        element.click()

    def click_TweetsReplies(self):
        element = self.driver.find_element(*ProfilePageLocators.TweetsReplies)
        element.click()

    def click_Media(self):
        element = self.driver.find_element(*ProfilePageLocators.Meida)
        element.click()

    def click_Likes(self):
        element = self.driver.find_element(*ProfilePageLocators.Likes)
        element.click()

class EditProfilePage(BasePage):
    def enter_Name(self,str):
        element = self.driver.find_element(*EditProfilePageLocators.Name)
        element.send_keys(str)
    
    def enter_Bio(self,str):
        element = self.driver.find_element(*EditProfilePageLocators.Bio)
        element.send_keys(str)

    def enter_Location(self,str):
        element = self.driver.find_element(*EditProfilePageLocators.Location)
        element.send_keys(str)

    def enter_Website(self,str):
        element = self.driver.find_element(*EditProfilePageLocators.Website)
        element.send_keys(str)

    def enter_Date(self,str):
        element = self.driver.find_element(*EditProfilePageLocators.Save)
        element.send_keys(str)

    def click_Save(self):
        element = self.driver.find_element(*EditProfilePageLocators.Save)
        element.click()

class AdminPage(BasePage):
    def click_Home(self):
        element = self.driver.find_element(*AdminPageLocators.AdminHome)
        element.click()

    def click_Statistics(self):
        element = self.driver.find_element(*AdminPageLocators.Statistics)
        element.click()

    def click_Users(self):
        element = self.driver.find_element(*AdminPageLocators.Users)
        element.click()