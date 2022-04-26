import unittest
import page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



class TwitterHomePage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        s = Service('C:\Program Files (x86)/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        #self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        
        #s = Service('C:\Program Files (x86)/msedgedriver.exe')
        #self.driver = webdriver.Edge(service=s)

        self.driver.get("http://www.twi-jay.xyz/")
        self.driver.maximize_window()
        
        
    def test_SignUpWithGoogle(self):
        

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Clicks On Sign Up with google button
        (main_page.click_SignUpWithGoogle_Button(),'Button Didnt Press')
        self.driver.get("https://accounts.google.com/o/oauth2/auth/identifier?redirect_uri=storagerelay%3A%2F%2Fhttp%2Flocalhost%3A3000%3Fid%3Dauth877532&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=335712697506-0rdelma7j4jgcc6bicuhnn20e2l8m0fm.apps.googleusercontent.com&ss_domain=http%3A%2F%2Flocalhost%3A3000&prompt&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow")
        #self.driver.implicitly_wait(100)
        Enter_Google_Email_Page = page.EnterGoogleEmailPage(self.driver)
        (Enter_Google_Email_Page.click_EnterEmail("mohamed.k.elrafie@gmail.com"))
        self.assertFalse(Enter_Google_Email_Page.click_Next())

        
       
        
        
       

    def test_SignUpWithPhoneMail(self):
        
        
        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Clicks On Sign Up with google button
        (main_page.click_SignUpWithPhoneOrMail(),'Button Didnt Press')
        signUpPhoneOrMail_Page = page.SignUpPhoneOrMailPage(self.driver)
        signUpPhoneOrMail_Page.enter_Username("@OmarGabr")
        signUpPhoneOrMail_Page.enter_Email("omargabr63@yahoo.com")
        signUpPhoneOrMail_Page.enter_Password("abcdRefg123_")
        signUpPhoneOrMail_Page.enter_Date("2020-03-04")
        signUpPhoneOrMail_Page.enter_Name("Omar Gabr")
        signUpPhoneOrMail_Page.click_Next_1()
        signUpPhoneOrMail_Page.click_Next_2()
        self.driver.implicitly_wait(100)
        self.assertFalse(signUpPhoneOrMail_Page.SignUpButton())
        #self.driver.implicitly_wait(100)
        #self.assertFalse(signUpPhoneOrMail_Page.click_Next_3())

        
        

    '''def test_SignIn(self):
        #El Front end me7tageen yezawedo id le zorar el next 2esmo nexttButton

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Clicks On Sign Up with google button
        (main_page.click_SignIn(),'Button Didnt Press')
        signIn_Page = page.SignInPage(self.driver)
        signIn_Page.enter_EmailOrUsername("@OmarGabr")
        signIn_Page.click_Next()
        signIn_Page.enter_Password('abcdeFg123_')
        self.assertFalse(signIn_Page.click_LogIn())'''

        

    def test_SignInGoogle(self):
        
        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Clicks On Sign Up with google button
        (main_page.click_SignIn(),'Button Didnt Press')
        signIn_Page = page.SignInPage(self.driver)
        self.driver.implicitly_wait(100)
        signIn_Page.click_SignInGoogle()
        self.driver.get("https://accounts.google.com/o/oauth2/auth/identifier?redirect_uri=storagerelay%3A%2F%2Fhttp%2Flocalhost%3A3000%3Fid%3Dauth778568&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=335712697506-0rdelma7j4jgcc6bicuhnn20e2l8m0fm.apps.googleusercontent.com&ss_domain=http%3A%2F%2Flocalhost%3A3000&prompt&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow")
        Enter_Google_Email_Page = page.EnterGoogleEmailPage(self.driver)
        (Enter_Google_Email_Page.click_EnterEmail("mohamed.k.elrafie@gmail.com"))
        self.assertFalse(Enter_Google_Email_Page.click_Next())
        


        

    '''def test_SignIn_ForgetPassword2(self):
        main_page = page.MainPage(self.driver)
        #Clicks On Sign Up with google button
        main_page.click_SignIn(),'Button Didnt Press'
        signIn_Page = page.SignInPage(self.driver)
        signIn_Page.enter_EmailOrUsername("@OmarGabr")
        signIn_Page.click_Next()
        signIn_Page.click_ForgetPassword_2()
        self.driver.implicitly_wait(100)
        signIn_Page.enter_Username2("@OmarGabr")
        signIn_Page.enter_Email2("hello.hello@gmail.com")
        self.assertFalse(signIn_Page.click_Search())
        #self.assertFalse(signIn_Page.click_next_2())'''


    def test_HomePage_Tweet(self):
        self.driver.get("http://www.twi-jay.xyz/home")
        Main_Page = page.MainPage2(self.driver)
        Main_Page.click_Home()
        home_page = page.HomePage(self.driver)
        home_page.enter_Tweet("Hello World")
        self.assertFalse(home_page.click_Tweet())
        

    def test_ExploreSearch(self):
        self.driver.get("http://www.twi-jay.xyz/home")
        Main_Page = page.MainPage2(self.driver)
        Main_Page.click_Explore()
        explore_page = page.ExplorePage(self.driver)
        explore_page.enter_Search("hELLO WorLD")
        self.assertFalse(explore_page.click_SearchButton())

    '''def test_Notifications(self):
        self.driver.get("http://localhost:3000/home")
        Main_Page = page.MainPage2(self.driver)
        Main_Page.click_Notifications()
        notifications_page = page.NotificationsPage(self.driver)
        notifications_page.click_All()
        self.driver.back()
        self.driver.implicitly_wait(100)
        notifications_page.click_Mentions()'''
        
    def test_ProfileEdit(self):
        self.driver.get("http://www.twi-jay.xyz/home")
        Main_Page = page.MainPage2(self.driver)
        Main_Page.click_Profile()
        profile_page = page.ProfilePage(self.driver)
        profile_page.click_EditProfile()
        Edit_Page = page.EditProfilePage(self.driver)
        Edit_Page.enter_Name("Mohamed")
        Edit_Page.enter_Bio("Hello")
        Edit_Page.enter_Location("London")
        Edit_Page.enter_Website("Arsenal.com")
        Edit_Page.enter_Date("2022-04-06")
        self.assertFalse(Edit_Page.click_Save())

    def test_ProfileFollow(self):
        self.driver.get("http://www.twi-jay.xyz/home")
        Main_Page = page.MainPage2(self.driver)
        Main_Page.click_Profile()
        profile_page = page.ProfilePage(self.driver)
        profile_page.click_Followers()
        self.driver.get("http://www.twi-jay.xyz/Profile")
        self.assertFalse(profile_page.click_Following())


    def test_Admin(self):
        self.driver.get("http://www.twi-jay.xyz/adminPage")
        admin_page = page.AdminPage(self.driver)
        admin_page.click_Home()
        self.driver.implicitly_wait(100)
        admin_page.click_Statistics()
        self.driver.implicitly_wait(100)
        self.assertFalse(admin_page.click_Users())
        
        
        
        
        
        
    
        
        
        

        
















    def tearDown(self):
        self.driver.close()












if __name__ == "__main__":
    unittest.main()





    










