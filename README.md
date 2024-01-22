After running the code we observe that the order of stations is different:

DFS: ['Metrobudivnykiv', 'Zakhysnykiv Ukrainy', 'Beketova', 'Derzhprom', 'Naukova', 'Botanichnyy Sad', '23 Serpnya', 'Oleksiivska', 'Peremoga', 'University', 'Pushkinska', 'Kyivska', 'Barabashova', 'Pavlova', 'Studentska', 'Heroiv Pratsi', 'Istorychnyy Muzey', 'Maydan Konst', 'Gagarina Ave', 'Sportyvna', 'Zavod Malysheva', 'Turboatom', 'Sport Palace', 'Armiyska', 'Maselskogo', 'Traktornyy Zavod', 'Industrial', 'Tsentralnyy Rynok', 'Pivdennyy Vokzal', 'Kholodna Hora']

BFS: ['Metrobudivnykiv', 'Zakhysnykiv Ukrainy', 'Sportyvna', 'Beketova', 'Gagarina Ave', 'Zavod Malysheva', 'Derzhprom', 'Maydan Konst', 'Turboatom', 
'University', 'Naukova', 'Istorychnyy Muzey', 'Tsentralnyy Rynok', 'Sport Palace', 'Pushkinska', 'Botanichnyy Sad', 'Pivdennyy Vokzal', 'Armiyska', 'Kyivska', '23 Serpnya', 'Kholodna Hora', 'Maselskogo', 'Barabashova', 'Oleksiivska', 'Traktornyy Zavod', 'Pavlova', 'Peremoga', 'Industrial', 'Studentska', 'Heroiv Pratsi']

Based on the provided output we can conclude that:

- DFS explores deeply along one branch of the graph before moving on to the next branch.
- BFS explores all the neighbors of a node before moving on to the next level of nodes,  resulting in a more orderly path.

Thus the key difference lies in the exploration strategy. DFS goes deep before branching, while BFS explores level by level.
In the context of a metro graph, BFS tends to find more direct routes between stations.
