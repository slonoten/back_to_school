using System.Text;

Console.WriteLine(Factorial.Calc(200000));


/// <summary>
/// Calculates factorial using only Int32
/// </summary>
class Factorial
{
    public static String Calc(int x)
    {
        checked
        {
            if (System.Int32.MaxValue / x < 100)
            {
                throw new Exception("Too big");
            }

            // Calculate base for module operations
            var @base = 10;
            var n = int.MaxValue / x;
            var numWidth = 1;
            while (n > 10)
            {
                @base *= 10;
                n /= 10;
                numWidth++;
            } 

            var acc = new List<int> {1}; // Storage for result values
            var shift = new List<int> {0}; // Storage for shift values
            var accLen = 1;

            for(var mult = 2; mult <= x; mult++)
            {
                for (var i = 0; i < acc.Count; i++)
                {
                    int value = acc[i] * mult;
                    acc[i] = value % @base;
                    shift[i] = value / @base;
                }
                if (shift[accLen - 1] > 0)
                {
                    acc.Add(0);
                    shift.Add(0);
                    accLen++;
                } 
                for (var i = 1; i < acc.Count; i++)
                {
                    int value = acc[i] + shift[i - 1];
                    acc[i] = value % @base;
                    shift[i] += value / @base;
                }
                if (shift[accLen - 1] > 0)
                {
                    acc.Add(shift[accLen - 1]);
                    shift.Add(0);
                    accLen++;
                } 
            }            

            var format = $"{{0:d{numWidth}}}";
            acc.Reverse();
            var sb = new StringBuilder();
            foreach(var num in acc)
            {
                sb.Append(string.Format(format, num));
            }

            return sb.ToString();
        }
    }
}


