import heapq

def dinosaur():
    word_count = {}
    with open('dataset1.csv', 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip().split(',')
            for word in line:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            line = f.readline()
    heap = []
    for i in word_count:
        heapq.heappush(heap, (-word_count[i], i))
    
    for i in range(3):
        count, word  = heapq.heappop(heap)
        print(-int(count), word)
    return heap


if __name__ == '__main__':
    print(dinosaur())

