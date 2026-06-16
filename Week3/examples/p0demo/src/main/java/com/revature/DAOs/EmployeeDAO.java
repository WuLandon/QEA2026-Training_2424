package com.revature.DAOs;

import com.revature.models.Employee;
import com.revature.utils.ConnectionUtil;

import java.sql.*;
import java.util.ArrayList;

public class EmployeeDAO implements EmployeeDAOInterface{
    @Override
    public ArrayList<Employee> getEmployees()
    {
        //instantiate a Connection object so that we can talk to the DB.
        try(Connection conn = ConnectionUtil.getConnection()){

            //A string that will represent our SQL statement
            String sql = "select * from employees;";

            Statement s = conn.createStatement();

            ResultSet rs = s.executeQuery(sql);

            ArrayList<Employee> employeeList = new ArrayList<>();

            while(rs.next()){
                Employee e = new Employee(
                        rs.getInt("employee_id"),
                        rs.getString("first_name"),
                        rs.getString("last_name")
                );
                employeeList.add(e);
            }
            return employeeList;

        } catch (SQLException e){
            e.printStackTrace();
        }
        return null;

    }

    @Override
    public Employee insertEmployee(Employee emp) {
        //instantiate a Connection object so that we can talk to the DB.
        try(Connection conn = ConnectionUtil.getConnection()){

            String sql = "insert into employees (first_name, last_name) values (?,?);";

            PreparedStatement ps = conn.prepareStatement(sql);

            ps.setString(1,emp.getFirst_name());
            ps.setString(2,emp.getLast_name());

            ps.executeUpdate();

            return emp;

        } catch (SQLException e){
            e.printStackTrace();
        }
        return null;
    }
}
