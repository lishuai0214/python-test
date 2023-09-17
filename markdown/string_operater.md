1. **len()**：返回字符串的长度。

   ```python
   text = "Hello, World!"
   length = len(text)  # 返回 13
   ```

2. **str()**：将其他数据类型转换为字符串。

   ```python
   num = 42
   text = str(num)  # 返回 "42"
   ```

3. **concatenation（连接）**：使用 `+` 运算符将两个字符串连接起来。

   ```python
   str1 = "Hello"
   str2 = "World"
   result = str1 + ", " + str2  # 返回 "Hello, World"
   ```

4. **索引和切片**：可以使用索引访问字符串中的单个字符，也可以使用切片来获取子字符串。

   ```python
   text = "Python"
   char = text[0]  # 返回 "P"
   substring = text[2:5]  # 返回 "tho"
   ```

5. **split()**：根据指定的分隔符将字符串拆分为子字符串，返回一个列表。

   ```python
   text = "apple,banana,cherry"
   fruits = text.split(",")  # 返回 ["apple", "banana", "cherry"]
   ```

6. **join()**：将一个列表（或其他可迭代对象）的元素连接成一个字符串。

   ```python
   fruits = ["apple", "banana", "cherry"]
   text = ",".join(fruits)  # 返回 "apple,banana,cherry"
   ```

7. **strip()**、**lstrip()**和**rstrip()**：移除字符串两侧、左侧或右侧的空格或指定字符。

   ```python
   text = "   Hello, World!   "
   stripped_text = text.strip()  # 返回 "Hello, World!"
   ```

8. **replace()**：替换字符串中的特定子字符串。

   ```python
   text = "I love programming in Python."
   new_text = text.replace("Python", "JavaScript")  # 返回 "I love programming in JavaScript."
   ```

9. **find()**和**index()**：查找子字符串在字符串中的位置。

   ```python
   text = "Hello, World!"
   position1 = text.find("World")  # 返回 7
   position2 = text.index("World")  # 返回 7
   ```

10. **count()**：统计字符串中特定子字符串的出现次数。

    ```python
    text = "Hello, Hello, Hello, World!"
    count = text.count("Hello")  # 返回 3
    ```

当然，Python还提供了许多其他有用的字符串操作函数和方法。以下是一些更多的示例：

11. **capitalize()**：将字符串的第一个字符大写，其余字符小写。

    ```python
    text = "hello, world!"
    capitalized_text = text.capitalize()  # 返回 "Hello, world!"
    ```

12. **title()**：将字符串中每个单词的首字母大写。

    ```python
    text = "hello, world!"
    title_text = text.title()  # 返回 "Hello, World!"
    ```

13. **isalpha()**：检查字符串是否只包含字母字符。

    ```python
    text = "Python"
    is_alpha = text.isalpha()  # 返回 True
    ```

14. **isdigit()**：检查字符串是否只包含数字字符。

    ```python
    text = "12345"
    is_digit = text.isdigit()  # 返回 True
    ```

15. **isalnum()**：检查字符串是否只包含字母和数字字符。

    ```python
    text = "Python3"
    is_alnum = text.isalnum()  # 返回 True
    ```

16. **islower()**和**isupper()**：检查字符串是否全小写或全大写。

    ```python
    text1 = "python"
    text2 = "PYTHON"
    is_lower = text1.islower()  # 返回 True
    is_upper = text2.isupper()  # 返回 True
    ```

17. **startswith()**和**endswith()**：检查字符串是否以特定前缀或后缀开始或结束。

    ```python
    text = "Hello, World!"
    starts_with = text.startswith("Hello")  # 返回 True
    ends_with = text.endswith("World!")  # 返回 True
    ```

18. **isnumeric()**：检查字符串是否只包含数值字符（包括Unicode数值字符）。

    ```python
    text = "12345"
    is_numeric = text.isnumeric()  # 返回 True
    ```

