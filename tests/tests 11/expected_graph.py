tree = """digraph tree {
1 [label=program];
1 -> 2;
2 [label=stmt];
2 -> 3;
3 [label=bind];
3 -> 4;
4 [label=id];
4 -> 5;
5 [label="Terminal: s"];
3 -> 6;
6 [label="Terminal: :="];
3 -> 7;
7 [label=expr];
7 -> 8;
8 [label=val];
8 -> 9;
9 [label=integer];
9 -> 10;
10 [label="Terminal: 1"];
1 -> 11;
11 [label="Terminal: ;"];
1 -> 12;
12 [label="Terminal: <EOF>"];
}
"""
