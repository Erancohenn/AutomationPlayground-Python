import tests.conftest as conf
from page_objects.ajax_data import AjaxData
from page_objects.class_attribute import ClassAttribute
from page_objects.click import Click
from page_objects.clinet_side_delay import ClientSideDelay
from page_objects.dynamic_id import DynamicID
from page_objects.dynamic_table import DynamicTable
from page_objects.hidden_layers import HiddenLayers
from page_objects.load_delay import LoadDelay
from page_objects.main import MainPage
from page_objects.mouse_over import MouseOver
from page_objects.non_breaking_space import NonBreakingSpace
from page_objects.overlapped import Overlapped
from page_objects.progress_bar import ProgressBar
from page_objects.sample_app import SampleApp
from page_objects.scrollbars import Scrollbars
from page_objects.text_input import TextInput
from page_objects.verify_text import VerifyText
from page_objects.visibility import Visibility

# page objects
dynamic_id_page = None
class_atrr_page = None
hidden_layers_page = None
click_page = None
ajax_data_page = None
dynamic_table_page = None
load_delay_page = None
non_breaking_page = None
overlapped_page = None
progress_bar_page = None
sample_app_page = None
scrollbars_page = None
test_input_page = None
verify_text_page = None
visibility_page = None
client_side_delay_page = None
mouse_over_page = None
main_page = None


class ManagePages:
    @staticmethod
    def init_pages():
        """
        Initiating pages from page objects
        """
        globals()['main_page'] = MainPage(conf.driver)
        globals()['dynamic_id_page'] = DynamicID(conf.driver)
        globals()['class_atrr_page'] = ClassAttribute(conf.driver)
        globals()['hidden_layers_page'] = HiddenLayers(conf.driver)
        globals()['click_page'] = Click(conf.driver)
        globals()['ajax_data_page'] = AjaxData(conf.driver)
        globals()['dynamic_table_page'] = DynamicTable(conf.driver)
        globals()['load_delay_page'] = LoadDelay(conf.driver)
        globals()['non_breaking_page'] = NonBreakingSpace(conf.driver)
        globals()['overlapped_page'] = Overlapped(conf.driver)
        globals()['progress_bar_page'] = ProgressBar(conf.driver)
        globals()['sample_app_page'] = SampleApp(conf.driver)
        globals()['scrollbars_page'] = Scrollbars(conf.driver)
        globals()['test_input_page'] = TextInput(conf.driver)
        globals()['verify_text_page'] = VerifyText(conf.driver)
        globals()['visibility_page'] = Visibility(conf.driver)
        globals()['mouse_over_page'] = MouseOver(conf.driver)
        globals()['client_side_delay_page'] = ClientSideDelay(conf.driver)



