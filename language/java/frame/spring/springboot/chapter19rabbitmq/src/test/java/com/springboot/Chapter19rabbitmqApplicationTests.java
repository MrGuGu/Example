package com.springboot;

import com.springboot.rabbit.Sender;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class Chapter19rabbitmqApplicationTests {

	@Autowired
	Sender sender;

	@Test
	public void contextLoads() {
		sender.send();
	}

}
