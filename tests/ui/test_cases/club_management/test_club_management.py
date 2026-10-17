import pytest
import allure

from ui.pom.pages.news_page import NewsPage
from ui.pom.pages.club_management.club_profile_page import ClubProfilePage


@pytest.mark.ui
@allure.epic("Club Management")
@allure.feature("Create club profile")
class TestClubManagement:

    @pytest.fixture(autouse=True)
    def setup(self, log_in_user):
        """Setup fixture to initialize the starting page object."""
        self.news_page: NewsPage = log_in_user

    @allure.story("User can create club profile")
    @pytest.mark.parametrize("club_profile", 
    [{
        "club name": "Test club",
        "phone": "+482345432",
        "email": "robert@test.pl",
        "website": "https://myclubpage.pl",
        "location": "Warszawa",
        "opening": "07:00",
        "closing": "20:00",
        "logo picture": "club_logo.png"
    }])
    def test_update_club_profile(self, club_profile):
        """
        E2E Test Specification:
        1. Navigate to create club profile
        2. Fill up form with basic data
        3. Set opening hours
        4. Add logo and club pictures
        5. Check if save alert appeared correctly
        6. Navigate to other context (news)
        7. Navigate to create club profile
        8. Check id data are save correctly
        """
        create_club_profile_page: ClubProfilePage = self.news_page.side_menu.go_to_create_club_profile()
        create_club_profile_page.update_club_basic_data(club_name =  club_profile.get("club name"),
                                                        phone= club_profile.get("phone"),
                                                        email = club_profile.get("email"),
                                                        website =  club_profile.get("website"),
                                                        location = club_profile.get("location")
                                                        )
        create_club_profile_page.update_opening_hours_mo_fr(club_profile.get("opening"),
                                                             club_profile.get("closing"))
        create_club_profile_page.update_logo_picture(picture_name=club_profile.get("logo picture"))

        create_club_profile_page.save_profile()

        assert create_club_profile_page.get_alert_message() == ClubProfilePage.SAVE_MESSAGE

        #create_club_profile_page.side_menu.go_to_news().side_menu.go_to_create_club_profile()





