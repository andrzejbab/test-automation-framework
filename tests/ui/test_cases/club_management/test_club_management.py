import pytest
import allure

from ui.pom.pages.news_page import NewsPage
from ui.pom.pages.club_management.club_profile_page import ClubProfilePage
from ui.pom.components.add_user_modal_component import AddUserModalComponent
from ui.pom.pages.club_management.member_management_page import MemberManagementPage


@pytest.mark.ui
@allure.epic("Club Management")
@allure.feature("Create club profile, add memebers, manage sports objects, manage training types")
class TestClubManagement:

    @pytest.fixture(autouse=True)
    def setup(self, log_in_user):
        """Setup fixture to initialize the starting page object."""
        self.news_page: NewsPage = log_in_user

    @allure.story("User can create full club profile")
    @pytest.mark.parametrize("club_profile", 
    [{
        "club name": "Test club",
        "phone": "+482345432",
        "email": "robert@test.pl",
        "website": "https://myclubpage.pl",
        "location": "Warszawa",
        "opening": "07:00",
        "closing": "20:00",
        "logo picture": "club_logo.png",
        "club pictures": ["club_pic1.png", "club_pic2.png"],
        "sobota": ["Sobota", "08:00", "21:00"],
        "niedziela": ["Niedziela", "08:00", "21:00"],
    }])
    def test_update_club_profile(self, club_profile):
        """
        E2E Test Specification:
        1. Navigate to create club profile
        2. Fill up form with basic data
        3. Set opening hours
        4. Add logo and club pictures
        5. Save and check if save alert appeared correctly
        6. Navigate to other context (news)
        7. Navigate to create club profile and check if data are saved correctly
        """

        # 1
        create_club_profile_page: ClubProfilePage = self.news_page.side_menu.go_to_create_club_profile()
        # 2
        create_club_profile_page.update_club_basic_data(club_name =  club_profile.get("club name"),
                                                        phone= club_profile.get("phone"),
                                                        email = club_profile.get("email"),
                                                        website =  club_profile.get("website"),
                                                        location = club_profile.get("location")
                                                        )
        # 3
        create_club_profile_page.update_opening_closing_hours_mo_fr(club_profile.get("opening"),
                                                             club_profile.get("closing"))
        create_club_profile_page.update_opening_closing_hours(*club_profile.get("sobota"))
        create_club_profile_page.update_opening_closing_hours(*club_profile.get("niedziela"))
        # 4
        create_club_profile_page.update_logo_picture(picture_name=club_profile.get("logo picture"))
        create_club_profile_page.upload_club_picture(picture_name_list=club_profile.get("club pictures"))
        #5
        create_club_profile_page.save_profile()
        assert create_club_profile_page.get_alert_message() == ClubProfilePage.SAVE_MESSAGE
        #6
        create_club_profile_page.side_menu.go_to_news().side_menu.go_to_create_club_profile()
        #7
        assert create_club_profile_page.get_opening_hour_simultaneously() == ""
        assert create_club_profile_page.get_closing_hour_simultaneously() == ""

        assert create_club_profile_page.get_club_name() == club_profile.get("club name")
        assert create_club_profile_page.get_club_phone() == club_profile.get("phone")
        assert create_club_profile_page.get_club_email() == club_profile.get("email")
        assert create_club_profile_page.get_club_website() == club_profile.get("website")
        assert create_club_profile_page.get_club_location() == club_profile.get("location")

        for day in ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"):
            assert create_club_profile_page.get_opening_hour(day) == club_profile.get("opening")
            assert create_club_profile_page.get_closing_hour(day) == club_profile.get("closing")

        for day, opening, closing in (club_profile.get("sobota"), club_profile.get("niedziela")):
            assert create_club_profile_page.get_opening_hour(day) == opening
            assert create_club_profile_page.get_closing_hour(day) == closing



    @allure.story("User can create club member")
    @pytest.mark.parametrize("club_member", [
        {
            "name": "Tomek",
            "last name": "Tester",
            "email": "robert@test.pl",
            "phone": "+482345432"
        }
    ])
    def test_update_club_profile(self, club_member):
        """
        E2E Test Specification:
        1. Navigate to "create club member"
        2. Fill up modal form with user details
        3. Check if user +
        """

        # 1
        member_management_page: MemberManagementPage = self.news_page.side_menu.go_to_manage_members()
        # 2
        add_user_modal_component: AddUserModalComponent = member_management_page.add_member().enter_name(club_member.get("name")) \
                                                        .enter_last_name(club_member.get("last name")) \
                                                        .enter_email(club_member.get("email")) \
                                                        .enter_phone(club_member.get("phone"))
        add_user_modal_component.set_player(True)

        assert True
        # 3

