import os
import shutil


def main():
    task_number = input("Enter task number: ")

    folder_name = f"s{task_number}"
    folder_path = os.path.join("./tasks/leetcode/", folder_name)

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    os.makedirs(folder_path)

    file1 = os.path.join(folder_path, f"s{task_number}.py")
    file2 = os.path.join(folder_path, f"test_{task_number}.py")

    open(file1, "w").close()
    test_content = f"""from tasks.leetcode.s{task_number}.s{task_number} import Solution
def test_numSpecial():
    s = Solution()
    assert ( s.numSpecial() == 1)
"""

    with open(file2, "w") as f:
        f.write(test_content)

    print(
        f"Created {folder_name}/ with {file1.split('/')[-1]} and {file2.split('/')[-1]}"
    )


if __name__ == "__main__":
    main()
