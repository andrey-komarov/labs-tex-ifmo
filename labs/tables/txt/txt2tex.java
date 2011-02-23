import java.io.*;
import java.util.*;

public class txt2tex implements Runnable {
	public static void main(String[] args) {
		new Thread(new txt2tex()).start();
	}

	BufferedReader br;
	StringTokenizer in;
	PrintWriter out;
	boolean fl;

	public String nextToken() throws IOException {
		while (in == null || !in.hasMoreTokens()) {
			if (in != null){
				out.println("\\\\");
				out.println("\\hline");
			}
			String ss = br.readLine();
			if (ss == null)
				ss = " ";
			in = new StringTokenizer(ss);
			if (ss == " "){
				fl = true;
				break;
			}
		}
		if (!fl)
			return in.nextToken();
		else
			return "";
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
		String s = "1";
		in = new StringTokenizer(br.readLine());
		out.print("\\begin{tabular}{|");
		for (int i = 0; i < in.countTokens(); i++){
			out.print("c|");
		}
		out.println('}');
		out.println("\\hline");
		while (s != ""){
			s = nextToken();
			if (fl)
				break;
			out.print(s);
			if (in.hasMoreTokens())
				out.print(" & ");
		}
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