package lab1;


public class Statistics {
	private double[] values;
	
	public Statistics(double[] vals) {
		this.values = vals;
	}
	
	double getMean()
    {
        double sum = 0.0;
        for(double a : values)
            sum += a;
        return sum/values.length;
    }

    double getVariance()
    {
        double mean = getMean();
        double temp = 0;
        for(double a :values)
            temp += (a-mean)*(a-mean);
        return temp/values.length;
    }

    double getStdDev()
    {
        return Math.sqrt(getVariance());
    }
}