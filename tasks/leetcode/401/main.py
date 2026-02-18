from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        bit_minutes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        bit_hours = {0: [], 1: [], 2: [], 3: []}

        def get_bits(val: int):
            count = 0
            for x in [32, 16, 8, 4, 2, 1]:
                count = count + (1 if (val & x) != 0 else 0)
            return count

        for i in range(12):
            bits = get_bits(i)
            bit_minutes[bits].append(i)
            bit_hours[bits].append(i)
        for i in range(11, 60):
            bits = get_bits(i)
            bit_minutes[bits].append(i)

        hours_start = max(turnedOn - 5, 0)
        hours_end = min(turnedOn, 3)
        variants = [[x, turnedOn - x] for x in range(hours_start, hours_end + 1)]
        print(variants)
        print(bit_hours)
        resp = []
        for h_bits, m_bits in variants:
            for hour in bit_hours[h_bits]:
                for minute in bit_minutes[m_bits]:
                    resp.append(str(hour) + ":" + str(minute).zfill(2))
        return resp


def test_longestBalanced():
    assert Solution().readBinaryWatch(1) == [
        "0:01",
        "0:02",
        "0:04",
        "0:08",
        "0:16",
        "0:32",
        "1:00",
        "2:00",
        "4:00",
        "8:00",
    ]
    assert sorted(Solution().readBinaryWatch(3)) == sorted(
        [
            "0:25",
            "0:26",
            "0:28",
            "0:35",
            "0:37",
            "0:38",
            "0:41",
            "0:42",
            "0:44",
            "0:49",
            "0:50",
            "0:52",
            "0:56",
            "1:03",
            "1:05",
            "1:06",
            "1:09",
            "1:10",
            "1:12",
            "1:17",
            "1:18",
            "1:20",
            "1:24",
            "1:33",
            "1:34",
            "1:36",
            "1:40",
            "1:48",
            "2:03",
            "2:05",
            "2:06",
            "2:09",
            "2:10",
            "2:12",
            "2:17",
            "2:18",
            "2:20",
            "2:24",
            "2:33",
            "2:34",
            "2:36",
            "2:40",
            "2:48",
            "3:01",
            "3:02",
            "3:04",
            "3:08",
            "3:16",
            "3:32",
            "4:03",
            "4:05",
            "4:06",
            "4:09",
            "4:10",
            "4:12",
            "4:17",
            "4:18",
            "4:20",
            "4:24",
            "4:33",
            "4:34",
            "4:36",
            "4:40",
            "4:48",
            "5:01",
            "5:02",
            "5:04",
            "5:08",
            "5:16",
            "5:32",
            "6:01",
            "6:02",
            "6:04",
            "6:08",
            "6:16",
            "6:32",
            "7:00",
            "8:03",
            "8:05",
            "8:06",
            "8:09",
            "8:10",
            "8:12",
            "8:17",
            "8:18",
            "8:20",
            "8:24",
            "8:33",
            "8:34",
            "8:36",
            "8:40",
            "8:48",
            "9:01",
            "9:02",
            "9:04",
            "9:08",
            "9:16",
            "9:32",
            "10:01",
            "10:02",
            "10:04",
            "10:08",
            "10:16",
            "10:32",
            "11:00",
        ]
    )
