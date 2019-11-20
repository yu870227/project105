using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using MySql.Data.MySqlClient;
using Newtonsoft.Json;
using System.Diagnostics;

public partial class _Default : System.Web.UI.Page
{
    static int a;
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        if (CheckBox1.Checked == true)
        {
            if (DropDownList1.SelectedIndex == 0)
            {
                Response.Write("<script language=javascript>alert('請選擇年分');</" + "script>");
            }
            else if (DropDownList2.SelectedIndex == 0)
            {
                Response.Write("<script language=javascript>alert('請選擇月分');</" + "script>");
            }
        }
        string ser = TextBox1.Text;
        string xv = "", yv = "", zv = "";
        int count = 0;
        if (ser != "")
        {
            for (int i = 0; i < 3; i++)
            {
                if (CheckBoxList1.Items[i].Selected == true)
                {
                    count++;
                }
                else
                {
                    a = i;
                }
            }
            string dbhost = "203.64.84.94";
            string dbuser = "Fish";
            string dbpass = "851217";
            string dbtable = "project105";
            string connstr = "server=" + dbhost + ";uid=" + dbuser + ";pwd=" + dbpass + ";database=" + dbtable;
            MySqlConnection conn = new MySqlConnection(connstr);
            MySqlCommand comm = conn.CreateCommand();
            String cmdText = "SELECT id,readable,rich,timely,name,url,date FROM disease_t WHERE Name LIKE '%" + ser + "%'";

            if (count == 1)
            {
                if (CheckBoxList1.Items[0].Selected == true)
                {
                    xv = "可讀度";
                }
                else if (CheckBoxList1.Items[1].Selected == true)
                {
                    xv = "豐富度";
                }
                else if (CheckBoxList1.Items[2].Selected == true)
                {
                    xv = "即時度";
                }
                Graph1D sel;
                List<Graph1D> tem = new List<Graph1D>();
                //String cmdText = "SELECT ID,Readable,Trust,Rich,Timly,Name,Url FROM diseaseheart_t WHERE Name LIKE '%" + ser + "%'";
                conn.Open();
                MySqlCommand cmd = new MySqlCommand(cmdText, conn);
                MySqlDataReader reader = cmd.ExecuteReader();
                int a1 = 0;
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        a1 = 0;
                        if (CheckBox1.Checked == true)
                        {
                            if (DropDownList1.SelectedIndex != 0)
                            {
                                if (DropDownList2.SelectedIndex != 0)
                                {
                                    if (search_time(reader.GetString(6)))
                                    {
                                        if (CheckBox2.Checked == true && a1 == 0)
                                        {
                                            if (search_school(reader.GetString(5)))
                                            {
                                                sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                                tem.Add(sel);
                                                a1 = 1;
                                            }
                                        }
                                        if (CheckBox3.Checked == true && a1 == 0)
                                        {
                                            if (search_hostpital(reader.GetString(5)))
                                            {
                                                sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                                tem.Add(sel);
                                                a1 = 1;
                                            }
                                        }
                                        if (CheckBox4.Checked == true && a1 == 0)
                                        {
                                            if (search_research(reader.GetString(5)))
                                            {
                                                sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                                tem.Add(sel);
                                                a1 = 1;
                                            }
                                        }
                                        if (CheckBox2.Checked == false && CheckBox3.Checked == false && CheckBox4.Checked == false && a1 == 0)
                                        {
                                            sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                            tem.Add(sel);
                                            a1 = 1;
                                        }
                                    }
                                }
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox2.Checked == true && a1 == 0)
                        {
                            if (search_school(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox3.Checked == true && a1 == 0)
                        {
                            if (search_hostpital(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox4.Checked == true && a1 == 0)
                        {
                            if (search_research(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox2.Checked == false && CheckBox3.Checked == false && CheckBox4.Checked == false && a1 == 0)
                        {
                            sel = SelectDataGrapg1D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                            tem.Add(sel);
                            a1 = 1;
                        }
                        sel = new Graph1D();
                        //if (CheckBoxList1.Items[0].Selected == true)
                        //{
                        //    xv = "可讀度";
                        //}
                        //else if (CheckBoxList1.Items[1].Selected == true)
                        //{
                        //    xv = "豐富度";
                        //}
                        //else if (CheckBoxList1.Items[2].Selected == true)
                        //{
                        //    xv = "即時度";
                        //}
                    }
                    reader.Close();
                    conn.Close();
                    if (tem.Count != 0)
                    {
                        ScriptManager.RegisterStartupScript(this, GetType(), "graph1", "graph1('" + xv + "','" + yv + "','" + JsonConvert.SerializeObject(tem) + "')", true);
                    }
                }
                else
                {
                    divProgress.Style["display"] = "inline";
                    cr_google(ser);
                    divProgress.Style["display"] = "none";
                    Button1_Click(sender, e);
                }
            }
            else if (count == 2)
            {
                int a1 = 0;
                Graph2D sel;
                List<Graph2D> tem = new List<Graph2D>();
                int num = 0;
                conn.Open();
                MySqlCommand cmd = new MySqlCommand(cmdText, conn);
                MySqlDataReader reader = cmd.ExecuteReader();
                if (a == 0)
                {
                    xv = "豐富度";
                    yv = "即時度";
                }
                else if (a == 1)
                {
                    xv = "可讀度";
                    yv = "即時度";
                }
                else if (a == 2)
                {
                    xv = "可讀度";
                    yv = "豐富度";
                }
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        a1 = 0;
                        num++;
                        //if (num > 55)
                        //{
                        //    break;
                        //}
                        if (CheckBox1.Checked == true)
                        {
                            if (DropDownList1.SelectedIndex != 0)
                            {
                                if (DropDownList2.SelectedIndex != 0)
                                {
                                    if (search_time(reader.GetString(6)))
                                    {
                                        if (CheckBox2.Checked == true && a1 == 0)
                                        {
                                            if (search_school(reader.GetString(5)))
                                            {
                                                sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                                tem.Add(sel);
                                                a1 = 1;
                                            }
                                        }
                                        if (CheckBox3.Checked == true && a1 == 0)
                                        {
                                            if (search_hostpital(reader.GetString(5)))
                                            {
                                                sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                                tem.Add(sel);
                                                a1 = 1;
                                            }
                                        }
                                        if (CheckBox4.Checked == true && a1 == 0)
                                        {
                                            if (search_research(reader.GetString(5)))
                                            {
                                                sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                                tem.Add(sel);
                                                a1 = 1;
                                            }
                                        }
                                        if (CheckBox2.Checked == false && CheckBox3.Checked == false && CheckBox4.Checked == false && a1 == 0)
                                        {
                                            sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                            tem.Add(sel);
                                            a1 = 1;
                                        }
                                    }
                                }
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox2.Checked == true && a1 == 0)
                        {
                            if (search_school(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox3.Checked == true && a1 == 0)
                        {
                            if (search_hostpital(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox4.Checked == true && a1 == 0)
                        {
                            if (search_research(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox2.Checked == false && CheckBox3.Checked == false && CheckBox4.Checked == false && a1 == 0)
                        {
                            sel = SelectDataGrapg2D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                            tem.Add(sel);
                            a1 = 1;
                        }
                    }
                    reader.Close();
                    conn.Close();
                    if (tem.Count != 0)
                    {
                        ScriptManager.RegisterStartupScript(this, GetType(), "graph2", "graph2('" + xv + "','" + yv + "',' " + JsonConvert.SerializeObject(tem) + "')", true);
                    }
                }
                else
                {
                    divProgress.Style["display"] = "inline";
                    cr_google(ser);
                    divProgress.Style["display"] = "none";
                    Button1_Click(sender, e);
                }
            }
            else if (count == 3)
            {
                xv = "可讀度";
                yv = "豐富度";
                zv = "即時度";
                int serchco = 0;
                Graph3D sel;
                List<Graph3D> tem = new List<Graph3D>();
                conn.Open();
                MySqlCommand cmd = new MySqlCommand(cmdText, conn);
                MySqlDataReader reader = cmd.ExecuteReader();
                int a1 = 0;
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        a1 = 0;
                        serchco++;
                        //if (serchco > 50)
                        //{
                        //    break;
                        //}
                        if (CheckBox1.Checked == true && a1==0)
                        {
                            if (DropDownList1.SelectedIndex != 0)
                            {
                                if (search_time(reader.GetString(6)))
                                {
                                    if (CheckBox2.Checked == true && a1 == 0)
                                    {
                                        if (search_school(reader.GetString(5)))
                                        {
                                            sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                            tem.Add(sel);
                                            a1 = 1;
                                        }
                                    }
                                    if (CheckBox3.Checked == true && a1 == 0)
                                    {
                                        if (search_hostpital(reader.GetString(5)))
                                        {
                                            sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                            tem.Add(sel);
                                            a1 = 1;
                                        }
                                    }
                                    if (CheckBox4.Checked == true && a1 == 0)
                                    {
                                        if (search_research(reader.GetString(5)))
                                        {
                                            sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                            tem.Add(sel);
                                            a1 = 1;
                                        }
                                    }
                                    if (CheckBox2.Checked == false && CheckBox3.Checked == false && CheckBox4.Checked == false && a1 == 0)
                                    {
                                        sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                        tem.Add(sel);
                                        a1 = 1;
                                    }
                                }
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox2.Checked == true && a1 == 0)
                        {
                            if (search_school(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox3.Checked == true && a1 == 0)
                        {
                            if (search_hostpital(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox4.Checked == true && a1 == 0)
                        {
                            if (search_research(reader.GetString(5)))
                            {
                                sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                                tem.Add(sel);
                                a1 = 1;
                            }
                        }
                        if (CheckBox1.Checked == false && CheckBox2.Checked == false && CheckBox3.Checked == false && CheckBox4.Checked == false && a1 == 0)
                        {
                            sel = SelectDataGrapg3D(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(5), reader.GetString(4));
                            tem.Add(sel);
                            a1 = 1;
                        }
                    }
                    reader.Close();
                    conn.Close();
                    if (tem.Count != 0)
                    {
                        ScriptManager.RegisterStartupScript(this, GetType(), "graph3", "graph3('" + xv + "','" + yv + "',' " + zv + "','" + JsonConvert.SerializeObject(tem) + "')", true);
                    }
                }
                else
                {
                    divProgress.Style["display"] = "block";
                    cr_google(ser);
                    divProgress.Style["display"] = "none";
                    Button1_Click(sender, e);
                }
            }
            else
            {
                string str = "請選擇一個";
                ScriptManager.RegisterStartupScript(this, GetType(), "alertshow", "alertshow('" + str + "')", true);
            }

        }
        else
        {
            string str = "請輸入關鍵字";
            ScriptManager.RegisterStartupScript(this, GetType(), "alertshow", "alertshow('" + str + "')", true);
        }

    }


    public class Graph1D
    {
        public int id;
        public float x, y;
        public string name,url;
        public Graph1D()
        {
        }
        public void NewData(int id, float x, float y, string url, string name)
        {
            this.id = id;
            this.x = x;
            this.y = y;
            //  this.ti = name;
            this.name = name;
            this.url = url;
        }

    }

    public class Graph2D
    {
        public int id;
        public float x, y;
        public string url;
        public string name;

        public Graph2D()
        { }
        public void NewData(int id, float x, float y, string url,string name)
        {

            this.id = id;
            this.x = x;
            this.y = y;
            this.url = url;
            this.name = name;
        }
    }

    public class Graph3D
    {
        public int id;
        public string style;
        public float x, y, z;
        public string h, url;
        public Graph3D()
        {

        }
        public void NewData(int id, float x, float y, float z, string style, string h, string url)
        {
            this.id = id;
            this.x = x;
            this.y = y;
            this.z = z;
            this.style = style;
            this.h = h;
            this.url = url;
        }
    }

    protected void CheckBoxList1_SelectedIndexChanged(object sender, EventArgs e)
    {
    }
    protected void CheckBox1_CheckedChanged(object sender, EventArgs e)
    {
        if (CheckBox1.Checked == true)
        {
            Panel3.Visible = true;
        }
        else
        {
            Panel3.Visible = false;
        }
    }
    protected Graph1D SelectDataGrapg1D(string id, string readable, string rich, string timely, string url, string name)
    {
        Graph1D sel;
        sel = new Graph1D();
        if (CheckBoxList1.Items[0].Selected == true)
        {
            sel.id = int.Parse(id);
            sel.x = float.Parse(readable);
        }
        else if (CheckBoxList1.Items[1].Selected == true)
        {
            sel.id = int.Parse(id);
            sel.x = float.Parse(rich);
        }
        else if (CheckBoxList1.Items[2].Selected == true)
        {
            sel.id = int.Parse(id);
            sel.x = float.Parse(timely);
        }
        sel.y = 0.02F;
        sel.url = url;
        sel.name = name.Replace("\"", " "); 
        return sel;

    }
    protected Graph2D SelectDataGrapg2D(string id, string readable, string rich, string timely, string url, string name)
    {
        Graph2D sel = new Graph2D();

        sel.id = int.Parse(id);
        if (a == 0)
        {
            sel.x = float.Parse(rich);
            sel.y = float.Parse(timely);
        }
        else if (a == 1)
        {
            sel.x = float.Parse(readable);
            sel.y = float.Parse(timely);
        }
        else if (a == 2)
        {
            sel.x = float.Parse(readable);
            sel.y = float.Parse(rich);
        }
        sel.url = url;
        sel.url = url;
        if (name.Length > 10)
        {
            string titlename = name.Substring(0, 10) + "...";
            sel.name = titlename.Replace("\"", "");
        }
        else
        {
            sel.name = name.Replace("\"", "");
        }
        return sel;
    }
    protected Graph3D SelectDataGrapg3D(string id, string readable, string rich, string timely, string url, string name)
    {
        Graph3D sel = new Graph3D();

        sel.id = int.Parse(id);
        if (readable.Length >= 5)
        {
            readable = readable.Substring(0, 5);
        }
        sel.x = float.Parse(readable);
        if (rich.Length >= 5)
        {
            rich = rich.Substring(0, 5);
        }
        sel.y = float.Parse(rich);
        if (timely.Length >= 5)
        {
            timely = timely.Substring(0, 5);
        }
        sel.z = float.Parse(timely);

        sel.style ="#7DC1FF";
        if (name.Length > 10)
        {
            name = name.Replace("\"","");
            sel.h = name.Substring(0, 10) + "...";
        }
        else
        {
            sel.h = name;
        }
        sel.url = url;
        return sel;
    }
    protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        String datem;
        int m;
        if (DropDownList1.SelectedIndex != 0)
        {
            DropDownList2.Enabled = true;
            DropDownList2.Items.Clear();
            DropDownList2.Items.Add(new ListItem("選擇月份", "0"));
            datem = DateTime.Now.ToString("MM");
            m = int.Parse(datem);
            int y = int.Parse(DateTime.Now.ToString("yyyy"));
            if (int.Parse(DropDownList1.SelectedValue) != int.Parse(DateTime.Now.ToString("yyyy")))
            {
                m = 12;
            }
            for (int i = 0; i < m; i++)
            {
                DropDownList2.Items.Add(new ListItem((i + 1).ToString(), (i + 1).ToString()));
            }
        }
    }
    protected void Button2_Click(object sender, EventArgs e)
    {

    }
    protected void reset_Click(object sender, EventArgs e)
    {
        
    }
    protected void Button2_Click1(object sender, EventArgs e)
    {
        Response.Redirect("http://203.64.84.94:2222/105project/105project.aspx");
    }

    protected bool search_school(string url)
    {
        string cuturl;
        int firdot, secdot, s, ss;
        s = url.IndexOf("/www");
        ss = url.IndexOf("//");
        firdot = url.IndexOf(".");
        secdot = url.Substring(firdot + 1).IndexOf(".");
        if (s != -1)
        {
            cuturl = url.Substring(firdot, 2 + secdot);
        }
        else
        {
            cuturl = url.Substring(ss + 1, firdot - ss);
        }
        string dbhost = "203.64.84.94";
        string dbuser = "Fish";
        string dbpass = "851217";
        string dbtable = "105316105project";
        string connstr = "server=" + dbhost + ";uid=" + dbuser + ";pwd=" + dbpass + ";database=" + dbtable;
        MySqlConnection conn = new MySqlConnection(connstr);
        MySqlCommand comm = conn.CreateCommand();
        String cmdText = "SELECT id FROM school_t WHERE url LIKE '%" + cuturl + "%'";
        conn.Open();
        MySqlCommand cmd = new MySqlCommand(cmdText, conn);
        MySqlDataReader reader = cmd.ExecuteReader();

        //string a = reader.GetString(0);
        if (reader.HasRows)
        {
            reader.Close();
            conn.Close();
            return true;
        }
        reader.Close();
        conn.Close();
        return false;
    }
    protected bool search_hostpital(string url)
    {
        string cuturl;
        int firdot, secdot, s, ss;
        s = url.IndexOf("/www");
        ss = url.IndexOf("//");
        firdot = url.IndexOf(".");
        secdot = url.Substring(firdot + 1).IndexOf(".");
        if (s != -1)
        {
            cuturl = url.Substring(firdot, 2 + secdot);
        }
        else
        {
            cuturl = url.Substring(ss + 1, firdot - ss);
        }

        string dbhost = "203.64.84.94";
        string dbuser = "Fish";
        string dbpass = "851217";
        string dbtable = "105316120";
        string connstr = "server=" + dbhost + ";uid=" + dbuser + ";pwd=" + dbpass + ";database=" + dbtable;
        MySqlConnection conn = new MySqlConnection(connstr);
        MySqlCommand comm = conn.CreateCommand();
        String cmdText = "SELECT id FROM hospital_t WHERE url LIKE '%" + cuturl + "%'";
        conn.Open();
        MySqlCommand cmd = new MySqlCommand(cmdText, conn);
        MySqlDataReader reader = cmd.ExecuteReader();

        //string a = reader.GetString(0);
        if (reader.HasRows)
        {
            reader.Close();
            conn.Close();
            return true;
        }
        reader.Close();
        conn.Close();
        return false;
    }
    protected bool search_research(string url)
    {
        string cuturl;
        int firdot, secdot, s, ss;
        s = url.IndexOf("/www");
        ss = url.IndexOf("//");
        firdot = url.IndexOf(".");
        secdot = url.Substring(firdot + 1).IndexOf(".");
        if (s != -1)
        {
            cuturl = url.Substring(firdot, 2 + secdot);
        }
        else
        {
            cuturl = url.Substring(ss + 1, firdot - ss);
        }

        string dbhost = "203.64.84.94";
        string dbuser = "Fish";
        string dbpass = "851217";
        string dbtable = "105316120";
        string connstr = "server=" + dbhost + ";uid=" + dbuser + ";pwd=" + dbpass + ";database=" + dbtable;
        MySqlConnection conn = new MySqlConnection(connstr);
        MySqlCommand comm = conn.CreateCommand();
        String cmdText = "SELECT id FROM research_t WHERE url LIKE '%" + cuturl + "%'";
        conn.Open();
        MySqlCommand cmd = new MySqlCommand(cmdText, conn);
        MySqlDataReader reader = cmd.ExecuteReader();

        //string a = reader.GetString(0);
        if (reader.HasRows)
        {
            reader.Close();
            conn.Close();
            return true;
        }
        reader.Close();
        conn.Close();
        return false;
    }
    protected bool search_time(string date)
    {
        if (date.CompareTo("None") != 0)
        {
            string staryear = DropDownList1.SelectedValue;
            string starmonth = DropDownList2.SelectedValue;
            string year = date.Substring(0, 4);
            int datelong = date.Length;
            string month = date.Substring(5);
            month = month.Replace('月', ' ');

            if (int.Parse(staryear) == int.Parse(year))
            {
                if (int.Parse(month) >= int.Parse(starmonth))
                {
                    return true;
                }
            }
            else if (int.Parse(staryear) < int.Parse(year))
            {
                return true;
            }
        }
        return false;
    }
    protected void cr_google(String search)
    {
        Process.Start("C:\\105專題\\105316126\\all_cr.exe",search);
    }
}