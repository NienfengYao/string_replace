# string_replace

* 這是一個 Python 程式碼範例，可以遍歷某個資料夾下的所有檔案，找尋特定文字並取代。
* example:
  ```
  ./str_replace.py ../root_dir/drivers/crypto/ 'https://support.company.com.' '(https:)support.company.com.' --exclude_dirs=fwtools
  ```
* 若遇到以下問題，應該是某個檔案中含特殊編碼無法被 utf-8 解譯。可以在原始檔案中移除這特殊字元，以便程式能正常執行
  ```
  Traceback (most recent call last):
  File "/mnt/server59/ryanyao/string_replace/./str_replace.py", line 53, in <module>
    main()
  File "/mnt/server59/ryanyao/string_replace/./str_replace.py", line 45, in main
    modified_files = replace_text_in_files(folder_path, search_text, replace_text, exclude_dirs)
  File "/mnt/server59/ryanyao/string_replace/./str_replace.py", line 22, in replace_text_in_files
    file_content = file.read()
  File "/usr/lib/python3.10/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0x91 in position 19105: invalid start byte
  ```
