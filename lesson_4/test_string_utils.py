
import pytest
from string_utils import StringUtils


string_util = StringUtils()


# Test Case 1: Тестирование функциональности "capitalize"
@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    ("peter", "Peter"),
    ("annMary", "Annmary"),
    ("mary Anne", "Mary anne"),
    ("ty'jan", "Ty'jan"),
    ("king1", "King1"),
    ("example-1", "Example-1"),
    ("Steve", "Steve"),
    ("GPS", "Gps"),
    ("trailing space  ", "Trailing space  "),
    # Негативные проверки:
    ("", ""), 
    ("123abc", "123abc"), 
    ("  leading space", "  leading space"),    
    ("éxample", "Éxample")  # other alphabets
])

def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result
    
    # Test Case 2: Тестирование функциональности "trim"
@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    ("  dog", "dog"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),
    (" Mary-Anne", "Mary-Anne"),
    ("   Peter1", "Peter1"),
    ("ca t", "ca t"),
    # Негативные проверки:
    ("", ""),
    ("monkey", "monkey"),
    ("123  ", "123  "),
    (1, 1),
    (0, 0)
])

def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result
    

# Test Case 3: Тестирование функциональности "to_list"
@pytest.mark.parametrize('string, divider, result', [
    # Позитивные проверки:
    ("dog,cat,bird", ",", ["dog", "cat", "bird"]),
    ("flower,tree,forest", ",", ["flower", "tree", "forest"]),
    ("pen;pencil;marker", ";", ["pen", "pencil", "marker"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    # Негативные проверки:
    ("", None, []),
    ])

def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    
    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)
    print(f"Actual result: {res}")
    assert res == result
    
 # Test Case 4: Тестирование функциональности "contains"
@pytest.mark.parametrize('string, symbol, result', [
      # Позитивные проверки:
    ("flower", "f", True),
    (" test", "t", True),
    ("space  ", "e", True),
    ("Mary-Anne", "-", True),
    ("123", "1", True),
    ("GPS", "P", True),
    ("", "", True),
      # Негативные проверки:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),  
    ("hello", "!", False), 
    ("hello", "", False),  
    ("", "x", False),  
    ("hello", "xyz", False),
    ("", "", False),
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result
    
# Test Case 5: Тестирование функциональности "delete_symbol"
@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("test", "t", "es"),
    ("Street", "r", "Steet"),
    ("Mountain", "M", "ountain"),
    ("123", "1", "23"),
    ("Mary-Anne", "-", "MaryAnne"),
    ("Sky Pro", "", "SkyPro"),
    ("plate", "pla", "te"),
    # Негативные проверки:
    ("spoon", "k", "spoon"),
    ("", "", ""),
    ("", "g", ""),
    ("milk", "", "milk"),
    ("park ", "", "park"),
    ("carpet  ", "r", "capet  ")
])

def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result
    
# Test Case 6: Тестирование функциональности "starts_with"
@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("table", "t", True),
    ("", "", True),
    ("Headphones", "H", True),
    (" car", "", True),
    ("Film  ", "F", True),
    ("Anne-Mary", "A", True),
    ("Mary Anne", "M", True),
    ("123", "1", True),
    ("list", "", True),
    # Негативные проверки:
    ("Headphones", "h", False),
    ("tea", "T", False),
    ("", "v", False),
    ("Test", "t", False),
    ("eleven", "n", False),
    ("twenty", "w", False)
])

def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result
    
    
# Test Case 7: Тестирование функциональности "end_with"
@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("winter", "r", True),
    ("GREAT", "T", True),
    ("", "", True),
    ("cat ", "", True),
    ("123", "3", True),
    ("Mary-Anne", "e", True),
    ("Anne Mary", "y", True),
    ("Peter1", "1", True),
    ("test", "", True),
    # Негативные проверки:
    ("morning", "P", False),
    ("evening", "e", False),
    ("door", "R", False),
    ("", "n", False)
])

def test_end_with(string, symbol, result):
    string_util=StringUtils()
    res=string_util.end_with(string, symbol)
    assert res==result
    
    
# Test Case 8: Тестирование функциональности "is_empty"
@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    ("", True),
    (" ", True),
    ("  ", True),
    # Негативные проверки:
    ("tree", False),
    (" flower", False),
    ("123", False),
    ("cat ", False)   
])

def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result
    

# Test Case 9: Тестирование функциональности "list_to_string"
@pytest.mark.parametrize('lst, joiner, result', [
    # Позитивные проверки:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Mary", "Anne"], "-", "Mary-Anne"),
    # Негативные проверки:
    ([], None, ""),
    ([], "*", "")
])

def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result
    

    
    
    
    
    
    