class Solution {

	public List<List<Long>> splitPainting(int[][] segments) {
		TreeMap<Integer, ArrayList<Integer>[]> map = new TreeMap<>();
		for (int i = 0; i < segments.length; i++) {
			if (!map.containsKey(segments[i][0])) {
				map.put(segments[i][0], new ArrayList[] { new ArrayList<>(), new ArrayList<>() });
			}
			map.get(segments[i][0])[0].add(i);
			if (!map.containsKey(segments[i][1])) {
				map.put(segments[i][1], new ArrayList[] { new ArrayList<>(), new ArrayList<>() });
			}
			map.get(segments[i][1])[1].add(i);
		}
		ArrayList<List<Long>> result = new ArrayList<>();
		long prev = 0, count = 0;
		for (int i : map.keySet()) {
			if (count > 0) {
				result.add(List.of(prev, (long) i, count));
			}
			for (int j : map.get(i)[0]) {
				count += segments[j][2];
			}
			for (int j : map.get(i)[1]) {
				count -= segments[j][2];
			}
			prev = i;
		}
		return result;
	}
}
