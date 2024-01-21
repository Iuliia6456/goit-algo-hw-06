After running the code we observe that the order of stations is different:

DFS: {'Istorychnyy Muzey', 'Peremoga', 'Derzhprom', 'Industrial', 'Traktornyy Zavod', 'Barabashova', 'Pivdennyy Vokzal', '23 Serpnya', 'Pavlova', 'Gagarina Ave', 'Zakhysnykiv Ukrainy', 'Botanichnyy Sad', 'Tsentralnyy Rynok', 'Studentska', 'Heroiv Pratsi', 'University', 'Pushkinska', 'Kholodna Hora', 'Naukova', 'Oleksiivska', 'Sport Palace', 'Armiyska', 'Metrobudivnykiv', 'Kyivska', 'Zavod Malysheva', 'Maselskogo', 'Beketova', 'Maydan Konst', 'Turboatom', 'Sportyvna'}

BFS: {'Istorychnyy Muzey', 'Peremoga', 'Derzhprom', 'Maydan Konst', 'Industrial', 'Traktornyy Zavod', 'Barabashova', 'Pivdennyy Vokzal', '23 Serpnya', 'Pavlova', 'Gagarina Ave', 'Zakhysnykiv Ukrainy', 'Botanichnyy Sad', 'Tsentralnyy Rynok', 'Studentska', 'Heroiv Pratsi', 'Pushkinska', 'Kholodna Hora', 'Naukova', 'Oleksiivska', 'Sport Palace', 'Armiyska', 'Metrobudivnykiv', 'Zavod Malysheva', 'Kyivska', 'Maselskogo', 'Beketova', 'University', 'Turboatom', 'Sportyvna'}

Based on the provided output we can conclude that:

- DFS explores deeply along one branch of the graph before moving on to the next branch.
- BFS explores all the neighbors of a node before moving on to the next level of nodes,  resulting in a more orderly path.

Thus the key difference lies in the exploration strategy. DFS goes deep before branching, while BFS explores level by level.
In the context of a metro graph, BFS tends to find more direct routes between stations.
