package lab1;

import java.math.BigDecimal;
import java.math.MathContext;
import java.util.ArrayList;




public class MarkingTrees {
	private static int RANDOM_1 = 1;
	private static int RANDOM_2 = 2;
	private static int RANDOM_3 = 3;
	private boolean[] tree;
	private ArrayList<Integer> indicies;
	private int[] pi;
	private int N;
	private int marked = 0, r2_count = 0;

	public static void main(String[] args) {
		MarkingTrees trees = new MarkingTrees();
				 
		int N = 1;
		int n = 127;
		double[] values = new double[N];
		for (int i = 0; i < N; i++) {
			values[i] = trees.do_stuff(n, RANDOM_3);
		 	trees.reset();
		}
		
		Statistics stat = new Statistics(values);
		
		double mean = stat.getMean();
		double deviation = stat.getStdDev();
		int scale = (int)(Math.floor(Math.max(Math.log10(mean), Math.log10(deviation))));
//		System.out.println(Math.log10(mean) + ", " + Math.log10(deviation) + ", " + scale);
		//scale = (scale > 6 ? 6: scale);
		mean /= Math.pow(10, scale);
		deviation /= Math.pow(10, scale);
//		System.out.println(mean + ", " + deviation);
		
		BigDecimal bd = new BigDecimal(deviation);
		bd = bd.round(new MathContext(1));
		double rounded = bd.doubleValue();

		bd = new BigDecimal(mean);
		bd = bd.round(new MathContext(2));
		double rounded_mean = bd.doubleValue();
		
		System.out.println("Mean rounds: " + rounded_mean + "+-" + rounded + (scale > 0 ? " x 10^" + scale : ""));
	}
	
	

	public void reset() {
		marked = 0;
		r2_count = 0;
	}

	public int do_stuff(int N, int r_type) {
		this.N = N;
		tree = new boolean[N];
		if (r_type == RANDOM_3) {
			indicies = new ArrayList<Integer>();
			for (int i = 0; i < tree.length; i++) {
				indicies.add(i);
			}
		}
		return traverse(r_type);
	}

	public int R1_getNext() {
		return (int) (Math.random() * N);
	}
	
	public int R2_getNext() {
		return pi[r2_count++];
	}
	
	public int R3_getNext() {
		int rnd = (int) (Math.random() * indicies.size());
		int next = indicies.get(rnd);
//		System.out.println("Next index: " + rnd + " next node: " + next);
		return next;
	}
	
	public void knuth() {
		pi = new int[N];
		for (int i = 0; i < pi.length; i++) {
			pi[i] = i;
		}
		for (int i = 0; i <= pi.length-2; i++) {
			int j = i + (int)(Math.random() * (pi.length - i));
			int temp = pi[i];
			pi[i] = pi[j];
			pi[j] = temp;
		}
	}

	public int traverse(int type) {
		int rounds = 0;
		if (type == 2) knuth();
		while (marked != N) {
			int next = 0;
			switch(type) {
			case 1:
				next = R1_getNext();
				break;
			case 2:
				next = R2_getNext();
				break;
			case 3:
				next = R3_getNext();
				break;
			}
			mark_stuff(next, type);
			rounds++;
		}
		System.out.println("Ended cycle with " + rounds + " rounds and marked: " + marked);
		return rounds;

	}

	public void mark_stuff(int node, int r_type) {
		if (marked != N && !tree[node]) {
			marked++;
			if (r_type == RANDOM_3) indicies.remove(new Integer(node));
			tree[node] = true;
			
			if (node != 0) {
				if (sibling(node)) {
					int parent = (node - 1) / 2;
					move_on(parent, r_type);
				}
				if (parent(node)) {
					int sibling = (node - 1) / 2;
					sibling = (sibling * 2 + 1 == node) ? sibling * 2 + 2 : sibling * 2 + 1;
					move_on(sibling, r_type);
				}
				
				if (left_child(node)) {
					int r_child = node * 2 + 2;
					move_on(r_child, r_type);
				}
				
				if (right_child(node)) {
					int l_child = node * 2 + 1;
					move_on(l_child, r_type);
				}
				
			} else {
				if (left_child(node)) {
					int r_child = node * 2 + 2;
					move_on(r_child, r_type);
				}
				
				if (right_child(node)) {
					int l_child = node * 2 + 1;
					move_on(l_child, r_type);
				}
			}
		}
	}
	
	private void move_on(int node, int type) {
		if (marked != N && !tree[node]) {
			mark_stuff(node, type);
//			System.out.println("Cascaded, marked node: " + node);
		}
	}

	private boolean sibling(int node) {
		int index = (node - 1) / 2;
		index = (index * 2 + 1 == node) ? index * 2 + 2 : index * 2 + 1;
		return tree[index];
	}

	private boolean parent(int node) {
		int index = (node - 1) / 2;
		return tree[index];
	}
	
	private boolean left_child(int node) {
		int index = node * 2 + 1;
		return index > N-1 ? false : tree[index];
	}
	
	private boolean right_child(int node) {
		int index = node * 2 + 2;
		return index > N-1 ? false : tree[index];
	}

}
