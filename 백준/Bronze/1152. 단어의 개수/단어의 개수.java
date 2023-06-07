import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputArr = br.readLine().split(" ");
		int answer = 0;
		for (String str : inputArr) {
			if (str != "") { 
				answer += 1;
			}
		}
		System.out.println(answer);
	}
}
