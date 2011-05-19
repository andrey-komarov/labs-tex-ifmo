import java.io.*;
import java.util.*;

public class txt2tex2 {
	public static void main(String[] args) {
		new txt2tex2().run();
	}

	BufferedReader br;
	StringTokenizer in;
	PrintWriter out;

	public String nextToken() throws IOException {
		while (in == null || !in.hasMoreTokens()) {
			in = new StringTokenizer(br.readLine(), "\t");
		}
		return in.nextToken();
	}

	public int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	public long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	public double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}

	public void solve() throws IOException {
		out.print("\\begin{tabular}{|");
		in = new StringTokenizer(br.readLine(), "\t");
		for (int i = 0; i < in.countTokens(); i++) {
			out.print("c|");
		}
		out.println('}');
		for (int i = 0; i < 25; i++) {
			if ((i == 0) || (i % 4 == 1))
				out.println("\\hline");
			else
				out.println("\\cline{2-4}");
			for (int j = 0; j < 11; j++) {
				if ((i == 0) || (i % 4 == 1)) {
					String s = nextToken();
					if ((i != 0) && ((j == 0) || (j > 3)))
						out.print("\\multirow{4}{*}{");
					out.print(s);
					if ((i != 0) && ((j == 0) || (j > 3)))
						out.print("}");
					out.print(' ');
					if (j < 10)
						out.print("& ");
					else {
						out.println("\\\\");
					}
					continue;
				}
				if ((j > 0) && (j < 4))
					out.print(nextToken());
				out.print(' ');
				if (j < 10)
					out.print("& ");
				else
					out.println("\\\\");

			}
		}
		out.println("\\hline");
		out.println("\\end{tabular}");
		out.println("\\par");

	}

	public void run() {
		try {
			br = new BufferedReader(new FileReader("txt2tex.in"));
			out = new PrintWriter("txt2tex.out");

			solve();

			out.close();
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(1);
		}
	}
}