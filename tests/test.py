import unittest
import os
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    import unittest
    import os
    from speciallecture.CSVPrinter import CSVPrinter

    class TestCSVPrinter(unittest.TestCase):

        def setUp(self):
            # 提示されたデータ（3行・4列）でテスト用ファイルを作成
            self.test_filename = "sample.csv"
            with open(self.test_filename, "w", encoding="utf-8") as f:
                f.write("aaa1,bbb1,ccc1,ddd1\n")
                f.write("aaa2,bbb2,ccc2,ddd2\n")
                f.write("aaa3,bbb3,ccc3,ddd3\n")

        def tearDown(self):
            # テスト終了後にサンプル用ファイルを自動削除
            if os.path.exists(self.test_filename):
                os.remove(self.test_filename)

        # テストケース1: 入力ファイルに含まれるすべての行を認識すること (3行)
        def test_case_1_row_count(self):
            printer = CSVPrinter(self.test_filename)
            lines = printer.read()
            self.assertEqual(3, len(lines))

        # テストケース2: カンマで区切られる中身が認識されること (4列 & 値の検証)
        def test_case_2_column_count_and_values(self):
            printer = CSVPrinter(self.test_filename)
            lines = printer.read()

            # 1. 各行がすべて4列であることを検証
            for row in lines:
                self.assertEqual(4, len(row))

            # 2. 1行目・1列目の値が "aaa1" であることを確認
            self.assertEqual("aaa1", lines[0][0])

            # 3. 全データの中身が完全に一致することを検証
            expected = [
                ["aaa1", "bbb1", "ccc1", "ddd1"],
                ["aaa2", "bbb2", "ccc2", "ddd2"],
                ["aaa3", "bbb3", "ccc3", "ddd3"]
            ]
            self.assertEqual(expected, lines)

        # テストケース3: 存在しないファイルが入力された場合，エラーを投げること
        def test_case_3_file_not_found(self):
            printer = CSVPrinter("non_existent_file.csv")
            with self.assertRaises(FileNotFoundError):
                printer.read()

    if __name__ == '__main__':
        unittest.main()
if __name__ == '__main__':
    unittest.main()