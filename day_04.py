import unittest
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TransformedBoard:
    rows: List[List[int]]
    columns: List[List[int]]


@dataclass
class NumberBoardRelation:
    board_index: int
    row_index: int
    column_index: int


class Solution:
    @staticmethod
    def giant_squid(draw_numbers: List[int], boards: List[List[List[int]]]) -> int:
        # Pre-process
        transformed_boards, number_board_relation = Solution.pre_process(boards=boards)

        # Start drawing
        for number in draw_numbers:
            for relation in number_board_relation[number]:
                board_index, row_index, column_index = (
                    relation.board_index,
                    relation.row_index,
                    relation.column_index,
                )
                board = transformed_boards[board_index]

                # Remove the number from row and column
                board.rows[row_index].remove(number)
                board.columns[column_index].remove(number)

                # Check if any board win or not
                if not board.rows[row_index] or not board.columns[column_index]:
                    return Solution.compute_result(number=number, board=board)

    @staticmethod
    def giant_squid_two(draw_numbers: List[int], boards: List[List[List[int]]]) -> int:
        # Pre-process
        transformed_boards, number_board_relation = Solution.pre_process(boards=boards)

        # Start drawing
        for number in draw_numbers:
            for relation in number_board_relation[number]:
                board_index, row_index, column_index = (
                    relation.board_index,
                    relation.row_index,
                    relation.column_index,
                )
                if board := transformed_boards.get(board_index):
                    # Remove the number from row and column
                    board.rows[row_index].remove(number)
                    board.columns[column_index].remove(number)

                    # Check if any board win or not
                    if not board.rows[row_index] or not board.columns[column_index]:
                        # Calculate the last winner board
                        if len(transformed_boards) == 1:
                            return Solution.compute_result(number=number, board=board)

                        del transformed_boards[board_index]

    @staticmethod
    def pre_process(boards: List[List[List[int]]]):
        transformed_boards = {}
        number_board_relation = defaultdict(list)

        # Pre-process
        for board_index, board in enumerate(boards):
            # Transform boards
            transformed_boards[board_index] = TransformedBoard(
                rows=[row[:] for row in board],
                columns=[[board[j][i] for j in range(5)] for i in range(5)],
            )

            for row_index, row in enumerate(board):
                for column_index, value in enumerate(row):
                    number_board_relation[value].append(
                        NumberBoardRelation(board_index, row_index, column_index)
                    )
        return transformed_boards, number_board_relation

    @staticmethod
    def compute_result(number: int, board: TransformedBoard) -> int:
        return number * sum(sum(_) for _ in board.rows)


class Tests(unittest.TestCase):
    @staticmethod
    def _read_input(input_string: str) -> Tuple[List[int], List[List[List[int]]]]:
        draw_numbers, *boards = input_string.split('\n\n')
        draw_numbers = [int(_) for _ in draw_numbers.split(',')]
        boards = [
            [[int(_) for _ in row.split()] for row in board.split('\n')]
            for board in boards
        ]
        return draw_numbers, boards

    def test_sample_input(self):
        draw_numbers, boards = self._read_input(
            '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,
        25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''
        )
        self.assertEqual(4512, Solution.giant_squid(draw_numbers=draw_numbers, boards=boards))
        self.assertEqual(1924, Solution.giant_squid_two(draw_numbers=draw_numbers, boards=boards))

    def test_real_problem(self):
        draw_numbers, boards = self._read_input(
            '''25,8,32,53,22,94,55,80,33,4,63,14,60,95,31,89,
        30,5,47,66,84,70,17,74,99,82,21,35,64,2,76,9,90,56,78,28,51,86,49,98,29,96,23,58,52,75,
        41,50,13,72,92,83,62,37,18,11,34,71,91,85,27,12,24,73,7,77,10,93,15,61,3,46,16,97,1,57,
        65,40,0,48,69,6,20,68,19,45,42,79,88,44,26,38,36,54,81,59,43,87,39,67

25 83 15 27 22
97 81 12 80 52
65 58 91 23 36
77 60 49 43 95
13 21 56 78 99

43 85 82 52 40
19 14 91  4  7
 6 87 64 26 56
94 58 81 98 90
18 72 23 37 20

 5 43 13 47 93
25 78 64 56 10
75 90 50 72 14
 9 29 58 79 62
69 66 88 35 16

73 13 35 91 24
66 37 39 88  7
55 36 41 81 85
29 49 70  4 23
98 69 84 56 87

30 44 76 87 57
67 24 63 38 99
41 69 35 60 78
32  6 88  9 55
46 75 77 13 22

29 68 51 92 64
50 65 86 22 98
66  6 44 53 87
54 63 25 59 14
96 52 90 58 71

68 73 79 50 98
10 94 53 46 88
59 78 35 71 15
42 67 82 17 92
40  1 83 61 16

44 64 97 63 93
32 84 55 70 24
29 67 68 86 18
90 72 42 21 88
53 40 85 27 11

45 31  6 30  3
66 16 73 65 25
48 41 98 27 55
39 17 19  8 24
85  2 28 63 13

86  3 20 41 53
98 45 63 74 47
87 68 97 13 42
58 73 48 35 17
91 38 55  4 34

13 44 26 77 23
51 88 41 42 93
12 56 38 87 73
60 19 55 99 21
 3 34 20 94 32

26 72 39 21 76
94 12  1 49 60
38 20 30 48 98
53 62 22 92 69
 7 88 57 81 13

99 20 70 52 12
23 28 45 66 41
92  8 55 22 36
14 78  9 46 18
21 87 89 27 68

76 92 45 53 98
56 91 72 19 35
25 59 42 90 68
47 97 30 65 95
94 60 52 36 54

 9 18 39 89 29
25 84 37 72 28
17 70 27 93  0
80 36 74 35 71
11 49 57 46  4

37 66 54 93 77
40 95 94 34 11
35 64 92 16 43
 9  6 83 32 29
 2 80 10 45 72

37 95 70 62  1
58 14 38 22 63
44  7 78 34 39
73 50 26  0 52
60 69 87 27 97

10  9 83 11  5
33 62 18 75 47
 3 86 36 26 91
39 80 14 67 15
74 95 88 37 57

 7 83 44 24 66
67 60 51 52 46
27 77 35 72 88
22 69  1 78 64
41 58 81 21  3

68 34 11 40 17
15 43  9 64 49
32 37 20 14 81
 3 87 72 16 51
25 77 58 10 52

89 61 97 14 56
32 90 98 69  4
88 58 51 76 66
15 62 35  7 29
95  8 33 73 22

25 59 40 71  8
36 42 47 67 19
93 50 80 98 79
72 97 68 81 39
56 91 12 95 53

65 90 44 88 66
43 23 35 18 77
 9 97 16 38 22
81 49 39 10 41
36 56 13 29 37

53 32  6 41  8
 4 38 88 29 37
58 54 15 83 12
13  1 98 85 23
69 49 26 64 70

66 33 15  7 77
26 16 79 28 58
69 96 14 44 61
43 75  0 97 36
59 41 22 24 87

90 54  4 62 63
 2 79 59  6 82
53 74 65 86 75
71 32 13 80 10
17  0 20 69 50

60  3 78  2 47
44 32 23 42 17
35 59 50 74 54
64 49 51  5 65
21 13 63 43 38

 6 53 57 18 33
26 31  9 44 34
81 21 39  2 52
95  5 43 46 91
98 71 59 30 48

13 31 91  1 67
96 35 20 19 40
87 27 78  9 22
11 45 38 46 51
72 68 23 25 85

99 97 85 86 20
92 16 60  6 67
18 87 93 79 53
 0 51 56 19 95
78 84 40 98 34

91 11  1 36 47
43 62 27 32 50
75 52 87 29 30
61 34 39 68 58
77 18 21 13 40

22 41 63 28 81
37 39 29 95 83
49 10 94  0 54
96 38 80 87  1
15 93 99 47 23

22 97 54 89 55
52 63 78 57 84
47 36 64 21 20
45 41 16 11 66
 3 98 10 99  1

26 15 89 54 86
10 60 52 64 74
40 91 24 51 66
95 43 29 34 85
88 18 97 31 53

61 96 63 89 12
57 28 29 23 53
82 40 56 44 13
50 73  0 30  4
79 78 64 37 26

29 60 24 73 38
69 94  6  9  1
97 40 27 26 86
59 52  4 15 96
61 63 55 66 85

98 39 56 63 58
54 88 41 48 65
85 28 14 29  2
20 70 46 72 93
75 59 36 57 71

38 27 60 37 44
98  9 13 45 57
 4 76 33  8 21
19  7 77 50 22
71 35 80 46 20

88 73 59 65 41
61 63 33 85 22
76 50 19 77 45
52 99  2  8 83
25 92 98 60 71

49 40 35 83 36
15 71 90 47 19
34 59 55 42 21
69  7 23  9 70
43 22 48 57 60

33  4 38 26 59
50 47 63 75 19
11 65 24 87 21
45 16 97 40 57
83 96 70 41 12

46 82 87 88  9
51 64 97  6 41
24 72 79 43 90
74 92 45 22 54
 1 95 80 55 14

86 52 90 19 85
25 67 30 84 56
66 71 39 74 96
93 46 89 72 29
97 40 99 62 44

82 87 79 63  1
27 61 30 26  6
76 59 56 44 36
72 12 88 92 33
93 78 66 67  9

96 81 75 42 20
87 13 35 79 77
 6 31 44 24 80
32 63 78  2 56
 1 46 40 99 14

55 24 10 61 89
 7 37 19 20 60
68 65 39 18 86
90 59 79 84 88
81 74 27 70 73

19 35 91 14 53
85 89  4 39 70
80 36  2 57 61
63 82 81 22 78
37 43 83 12 94

70 99 79 92 36
21 30 88 22 96
11 60 23 41 64
81 10 13 51 19
34 45 42 17 38

39 21 37  3  2
54 32 25 26 81
98 55 53 35 67
90 48 15 18 68
22 78 83 30 72

32 50 94 51 26
 1 82 86 75 89
27  6 16 57  3
91 66 30 39 25
 9 46 88 12 35

14 91 16 30 45
41 82 42 26 15
43 72 81 38 92
95 87  7 28 46
63 71 11 22 56

45 58 68 37 81
16 20 71 82 28
85 89 23 65 18
40 66 11 70 10
60 97 69 86 19

16 47 46 53 13
48 76 98 66 12
79 43 25 36 31
85  1 41  3 50
99 73 83 89 64

27 82 33 36 83
73 31 34  7 30
98 20 32 39 92
56 90 85 11 23
 6 89 44 87 50

18 58 84 47 15
63 16 22 65 72
82  4 55 13  8
19 86 11 52  3
54 80 39 97 12

73 85  3 24 37
 4  7 75 16 42
92 95 69 81 66
 0 40 12 18 49
26 38 56 25 35

66 91 90 41 44
89 47 23 24 18
 6 38 62  2 60
 1 29  8 53 70
76 50 85 34 81

 8 99 34 19 80
46  3 17 26 54
95 43 63 49 14
90 77  1 42 85
83 59 57 33 30

75 12  7 21 70
89 36 96 46 90
37 28 23 32 39
 2 18 81 11 57
15 24  0  9 65

 7 53  6 34 20
32 76 24 56 29
43 62 26 75 72
94 79 77 60 12
58 19 17 55  9

35 85 48 30 53
 3  0 98 74 37
55 29 81 86  2
22  7 33 62 94
 1 31 99 16 14

46 68  6 94 79
86 99 44 38 91
93 80 90 50 63
 2 71 65 23 39
43 31 20 82 28

20 64 92  2 23
87 28 99 93 59
70 30 39 33 51
13 27 95 90 29
24 47 83 48 60

64 93 47 22 27
 7 74 75 26 60
83  9  5 90 55
28 57 45 56 98
21 77 80  8 67

 1 11 79 36 24
27 37 50 69 98
 4 39 38  6 59
49 53 22 31 15
93 47 86 72 40

14 26 39 20 32
93 89 19 67 92
15 16 96 50 51
 2 86 97 54  5
25  8 72  4  1

32 64 27 13 63
70 36 95  9 80
 2 76 10 16  0
52 18 12 97 33
71 82 72 15 99

57 82 29  0 83
68 33 31 21 60
 7  2 27 44 89
15 88 71 70 52
97  3 63 66 59

45 94 12 48 24
 2 38 69  6 31
44 99 52 27 43
13 74 10 67 76
35 20 25 86 19

18 26 30 38 32
 0 27 82 55 72
53 20 19 58 84
80 76  2 97  4
61 24  3 73 92

91 85 95 12 11
94 49 41 31 47
98  9 56 55  3
42 22 19 72 68
59 54 88 50 16

51 68 98 11 48
45 17 81 10 94
38 69 42 40 67
 1 20 12 27 32
 8 44 41 79 62

47 65 41 60 12
92 43 94  1 86
18 63 26 46 71
62 21 11 80 98
23 40 67 77 89

78 67 20 48 53
99 10 38 51  7
62 89 87 68 93
31 55 80 69 29
36 74 88 44 11

39 27 82 95 52
53 75 34 35 41
 0 94 30 62 13
20 77  2  8 12
44 32 68 17 99

37 48  9 29 94
34 23 66 93 86
33 10 87 61 20
 1 41 35 80 19
83 96 47  2 76

62 25  0 47 39
96 24 99 73 61
51 72  9 21 20
97 71 19 83 78
46 34 44 48  1

60 63 97 56 96
 1 11 70 59  4
21 43  8 36 46
80 88 76 68 37
86  5 12 15 73

90 94 39 24 89
71 31 10 51 97
16 54 52 36 98
48  7 77 84 57
88  9 92  0 66

43 45 33  1 26
56 22  8 78 92
60 51 96  7 58
84 31 88 12 73
76 25 63 87 37

68 62 15 30 18
 5 49 23 13 73
45 67 50 35 86
85 31 53 27 32
 4  1 90 10  2

13 23 41 82 40
69 12 17  0 34
 4 91 71 21 67
53 87 36 80  6
83 25 92 29 56

61 95 19 53 22
50 40 66 58 79
92 33 47 45 14
54 32 12 48 78
89 28 82 80 21

18 35 15 51 50
41 29 46 22 79
34 97 92 75 87
99 76 42  6 58
86 10 91 21 67

51 27 94 66 64
83 26 45 87 41
61 77 68 17 99
74 93 19 28 50
12 69 44 63 10

15 10 47 79 12
90 20 18 19 64
61  6 33 29 52
92 37 43 49 13
91  4 50 65 53

35 80 88 72 81
22 84 51 96 25
 4 47 70 27 36
62 54 78 11  1
 5  0  6 19 53

83 54  4 26 86
63 11 50 46 96
58 99 23 18 82
14 57 77 98 72
43 34 25 65  1

73 58 62  8 61
 0 13 16 82 79
67 37 93 30 31
27  7 59 15 72
68 88 81 49 60

72 56 70 24 18
53 91 95 11 65
63 67 49 22 74
59 25 94 20 97
 6 73 52 47 38

18 46 93 87 51
24 28 10 30 38
82  2 40 17 76
81 39 97 48  5
19  0 27 74 63

59 95 47 41 28
31 57 15  5 40
21 72 56 99 17
37 52 27 48 33
50 53  8 73 68

10 21 79 71  5
40 92 54 97 46
45 15  9 42 50
68 81 90 47 99
44  2 64 27 69

 4 23 59 88 60
39 16 28 56 90
94 78 57 53 46
20 14 51 44 99
91 17  7 83 84

74 19 24 39 16
44 62 61 99 42
65 63 50 78 38
27 49 86 80 33
66 30  2 31 83

87 45 18 99  4
89 78 27 90 34
72  6 46 16 57
60 41 33 82 62
48 20 55 32 14

97 20 60 49 50
35  4 90 67 52
66 72 92 13 30
85 41 62 77 16
64 22 40 51 43

31 25 67  3 56
 1 60 89 98 15
73 24 41 35 12
26 83 62 17 79
95 65 84 14  0

15 71 52 81 45
99 48 65 79  4
85 36 37 87 64
61 95  6 27 34
17 14 43 60 92

59 93 18 63 19
92 14 61 13 26
39 70  2 58  6
68 57 89 81  4
55 98 79 85  3'''
        )
        print(Solution.giant_squid(draw_numbers, boards))
        print(Solution.giant_squid_two(draw_numbers, boards))
